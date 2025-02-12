import logging
import psycopg2
from psycopg2 import sql
import requests
import re
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from config2 import DB_CONFIG,OLD_TABLE_NAME,NEW_TABLE_NAME, TABLE_FIELDS, MODERATE_HATE_SPEECH_API_TOKEN
nltk.download('vader_lexicon')
logging.basicConfig(filename='script1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
            return False, None

        try:
            response_json = response.json()
            class_value = response_json.get("class")
            confidence_value = response_json.get("confidence")
            if class_value == "flag" and confidence_value is not None and float(confidence_value) > CONF_THRESHOLD:
                logging.info("Hate speech detected: %s with confidence %s", comment, confidence_value)
                return True, confidence_value
            return False, confidence_value
        except requests.exceptions.JSONDecodeError:
            logging.error(f"Failed to decode JSON response: {response.text}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    return False, None

def clean_comment(comment):
    comment_without_links = re.sub(r'https?://\S+', '', comment)
    cleaned_comment = re.sub(r'[^a-zA-Z0-9\s]', '', comment_without_links).lower()
    return cleaned_comment

def create_table(cursor, table_name):
    create_table_query = sql.SQL("""
        CREATE TABLE IF NOT EXISTS {} (
            comment_id TEXT PRIMARY KEY,
            original_comment TEXT,
            cleaned_comment TEXT,
            is_hate_speech BOOLEAN,
            hate_speech_confidence DOUBLE PRECISION,
            sentiment TEXT,
            sentiment_score DOUBLE PRECISION
        )
    """).format(sql.Identifier(table_name))
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
    create_table(cursor, NEW_TABLE_NAME)
    table_fields = TABLE_FIELDS.get(OLD_TABLE_NAME, None)
    if table_fields is None:
        logging.error("Table fields not defined for table: %s", OLD_TABLE_NAME)
        return
    id_field = table_fields["id_field"]
    text_field = table_fields["text_field"]
    select_query = sql.SQL("SELECT {}, {} FROM {}").format(
        sql.Identifier(id_field),
        sql.Identifier(text_field),
        sql.Identifier(OLD_TABLE_NAME)
    )
    cursor.execute(select_query)
    comments = cursor.fetchall()
    for comment_id, comment_text in comments:
        if is_comment_id_present(cursor, NEW_TABLE_NAME, comment_id):
            logging.info("Comment ID %s already present, skipping.", comment_id)
            continue
        cleaned_comment = clean_comment(comment_text)
        is_hate_speech, confidence_value = hs_check_comment(cleaned_comment)
        sentiment, sentiment_score = analyze_sentiment(cleaned_comment)
        insert_query = sql.SQL("""
            INSERT INTO {} (comment_id, original_comment, cleaned_comment, is_hate_speech, hate_speech_confidence, sentiment, sentiment_score)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """).format(sql.Identifier(NEW_TABLE_NAME))
        cursor.execute(insert_query, (comment_id, comment_text, cleaned_comment, is_hate_speech, confidence_value, sentiment, sentiment_score))
        if c % 1000 == 0:
            connection.commit()
    connection.commit()
    connection.close()

def analyze_sentiment(comment):
    if isinstance(comment, str):
        analyzer = SentimentIntensityAnalyzer()
        sentiment_scores = analyzer.polarity_scores(comment)
        if sentiment_scores['compound'] >= 0.05:
            logging.info("Positive sentiment detected: %s with score %s", comment, sentiment_scores['compound'])
            return 'positive', sentiment_scores['compound']
        elif sentiment_scores['compound'] <= -0.05:
            logging.info("Negative sentiment detected: %s with score %s", comment, sentiment_scores['compound'])
            return 'negative', sentiment_scores['compound']
        else:
            logging.info("Neutral sentiment detected: %s with score %s", comment, sentiment_scores['compound'])
            return 'neutral', sentiment_scores['compound']
    else:
        return 'not a string', None

if __name__ == "__main__":
    process_comments()
