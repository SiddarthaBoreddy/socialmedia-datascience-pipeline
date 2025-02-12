import logging
import psycopg2
from psycopg2 import sql
import requests
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from langdetect import detect
from config import DB_CONFIG, OLD_TABLE_CONFIG, NEW_TABLE_CONFIG, MODERATE_HATE_SPEECH_API_TOKEN


nltk.download('vader_lexicon')
logging.basicConfig(filename='script2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
c = 0
def hs_check_comment(comment):
    CONF_THRESHOLD = 0.9
    data = {
        "token": MODERATE_HATE_SPEECH_API_TOKEN,
        "text": comment
    }
    try:
        response = requests.post("https://api.moderatehatespeech.com/api/v1/moderate/", json=data)
        response.raise_for_status() 
        if not response.text:
            logging.warning("Empty JSON response, skipping.")
            return False
        try:
            response_json = response.json()
            class_value = response_json.get("class")
            confidence_value = response_json.get("confidence")
            if class_value == "flag" and confidence_value is not None and float(confidence_value) > CONF_THRESHOLD:
                logging.info("Hate speech detected: %s", comment)
                return True
            return False
        except requests.exceptions.JSONDecodeError:
            logging.error(f"Failed to decode JSON response: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    return False

def clean_comment(comment):
    comment_without_links = re.sub(r'https?://\S+', '', comment)
    cleaned_comment = re.sub(r'[^a-zA-Z0-9\s]', '', comment_without_links).lower()
    try:
        language = detect(cleaned_comment)
        logging.info("Detected language: %s", language)
    except Exception as e:
        logging.error("Language detection error: %s", str(e))
        language = 'unknown'
    return cleaned_comment, language

def create_table(cursor, table_name, columns):
    column_definitions = [
        sql.Identifier(column_name) + sql.SQL(' ') + sql.SQL(data_type)
        for column_name, data_type in columns.items()
    ]
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            {}
        )
    """).format(
        sql.Identifier(table_name),
        sql.SQL(', ').join(column_definitions)
    )
    print(create_table_query.as_string(cursor))
    cursor.execute(create_table_query)

def is_comment_id_present(cursor, table_name, comment_id):
    select_query = sql.SQL("SELECT EXISTS(SELECT 1 FROM {} WHERE comment_id = %s)").format(
        sql.Identifier(table_name)
    )
    cursor.execute(select_query, (comment_id,))
    return cursor.fetchone()[0]

def process_comments():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    create_table(cursor, NEW_TABLE_CONFIG["name"], NEW_TABLE_CONFIG["columns"])
    select_query = sql.SQL("SELECT {} FROM {}").format(
        sql.SQL(', ').join(map(sql.Identifier, OLD_TABLE_CONFIG["columns"])),
        sql.Identifier(OLD_TABLE_CONFIG["name"])
    )
    cursor.execute(select_query)
    comments = cursor.fetchall()
    for comment_data in comments:
        comment_id = comment_data[0]
        video_id = comment_data[1]
        comment_text = comment_data[2]
        if is_comment_id_present(cursor, NEW_TABLE_CONFIG["name"], comment_id):
            logging.info("Comment ID %s already present, skipping.", comment_id)
            continue
        cleaned_comment, language = clean_comment(comment_text)
        if language.lower() == 'en':
            is_hate_speech = hs_check_comment(cleaned_comment)
            sentiment = analyze_sentiment(cleaned_comment)
            insert_query = sql.SQL("""
                INSERT INTO {} ("comment_id", "video_id", "original_comment", "cleaned_comment", "is_hate_speech", "sentiment", "language")
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """).format(sql.Identifier(NEW_TABLE_CONFIG["name"]))
            values = (comment_id, video_id, comment_text, cleaned_comment, is_hate_speech, sentiment, language)
            cursor.execute(insert_query, values)
            if c % 1000 == 0:
                connection.commit()
    connection.commit()
    connection.close()

def analyze_sentiment(comment):
    if isinstance(comment, str):
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(comment)
        if sentiment_scores['compound'] >= 0.05:
            logging.info("Positive sentiment detected: %s", comment)
            return 'positive'
        elif sentiment_scores['compound'] <= -0.05:
            logging.info("Negative sentiment detected: %s", comment)
            return 'negative'
        else:
            logging.info("Neutral sentiment detected: %s", comment)
            return 'neutral'
    else:
        return 'not a string'

if __name__ == "__main__":
    process_comments()
