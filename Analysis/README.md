# 📊 Sentiment Analysis & Hate Speech Detection  

## 📖 Overview  

This module performs **sentiment analysis and hate speech detection** on collected comments from **Reddit and YouTube**. It uses **Natural Language Processing (NLP)** techniques to classify sentiment and identify hate speech.  

This analysis is part of a larger **3-part project**, where:  
- **Part 1 (Crawler)** → Fetches data from Reddit & YouTube.  
- **Part 2 (Analysis)** → Processes and analyzes sentiment and hate speech.  
- **Part 3 (Web Visualization)** → Presents insights on a web page.  

---  

## 🛠 Technologies Used  

- **Python** – Core implementation language.  
- **NLTK (Natural Language Toolkit)** – Used for sentiment analysis.  
- **VADER Sentiment Analyzer** – Determines the polarity of comments.  
- **Hate Speech API** – Identifies and flags potential hate speech.  
- **PostgreSQL** – Stores sentiment and hate speech analysis results.  
- **Matplotlib & Pandas** – Used for data visualization in Jupyter Notebook.  

---  

## 📌 Features  

✅ **Sentiment Classification** – Determines if a comment is positive, neutral, or negative.  
✅ **Hate Speech Detection** – Uses an external API to flag offensive content.  
✅ **Data Cleaning & Preprocessing** – Removes URLs, special characters, and non-English text.  
✅ **Stores Processed Data in PostgreSQL** – Ensures structured and queryable results.  
✅ **Visualizes Sentiment Trends** – Generates bar charts and time-series plots for analysis.  

---  

## 📂 Project Structure  

```
📁 Analysis/
│── an_all.py            # Processes Reddit sentiment & hate speech analysis
│── Analysis.yt.py       # Processes YouTube sentiment & hate speech analysis
│── plot.ipynb           # Jupyter notebook for visualization
│── README.md            # Project documentation
```  

---  

## 🚀 How It Works  

### **1️⃣ Prepare the Database**  
Ensure PostgreSQL is running and create the necessary tables:  

```sql
CREATE TABLE analyzed_comments (
    comment_id TEXT PRIMARY KEY,
    original_comment TEXT,
    cleaned_comment TEXT,
    is_hate_speech BOOLEAN,
    hate_speech_confidence DOUBLE PRECISION,
    sentiment TEXT,
    sentiment_score DOUBLE PRECISION
);
```  

### **2️⃣ Run Sentiment & Hate Speech Analysis**  
```sh
python an_all.py   # Processes Reddit comments  
python Analysis.yt.py  # Processes YouTube comments  
```  
These scripts:  
- Fetch comments from the database.  
- Clean and preprocess text data.  
- Analyze sentiment and flag hate speech.  
- Store results back into PostgreSQL.  

### **3️⃣ Generate Visualizations**  
```sh
jupyter notebook plot.ipynb
```  
This will generate charts showing:  
- Sentiment distribution across platforms.  
- Trends in hate speech detection.  
- Daily comment activity and analysis.  

---  

## 🔐 Data Considerations  

- **False Positives in Hate Speech** – Some flagged comments may not be actual hate speech.  
- **Language Detection** – Only processes English text to ensure sentiment accuracy.  
- **Bias in Sentiment Analysis** – Based on the limitations of VADER's pre-trained model.  

---  

## 🔮 Future Enhancements  

🔹 **Train a Custom Sentiment Model** for higher accuracy.  
🔹 **Improve Hate Speech Detection** by integrating multiple sources.  
🔹 **Multi-Language Support** for processing non-English comments.  
🔹 **More Advanced NLP Techniques** like BERT for better sentiment classification.  

---  

## 📜 References  

- [NLTK Sentiment Analysis](https://www.nltk.org/api/nltk.sentiment.html)  
- [Hate Speech Detection API](https://moderatehatespeech.com/)  
- [Matplotlib Visualization Guide](https://matplotlib.org/stable/contents.html)  

---  

## 📧 Contact  

**Author:** Siddartha Reddy Boreddy  
📍 **SUNY Binghamton**  
✉️ **Email:** sboreddy@binghamton.edu 

---  

### ⭐ If you find this project helpful, feel free to star the repository! 🚀  
