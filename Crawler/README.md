# 🕵️‍♂️ Web Crawler for Reddit & YouTube  

## 📖 Overview  

This module implements a **web crawler** that collects **comments and posts** from **Reddit and YouTube** using their respective APIs. The extracted data is stored in a **PostgreSQL database** for further analysis.  

This crawler is part of a larger **3-part project**, where:  
- **Part 1 (Crawler)** → Fetches data from Reddit & YouTube.  
- **Part 2 (Analysis)** → Processes and analyzes the collected data.  
- **Part 3 (Web Visualization)** → Presents insights on a web page.  

---  

## 🛠 Technologies Used  

- **Python** – Core implementation language.  
- **Reddit API** – Fetches comments and posts from subreddits.  
- **YouTube API** – Fetches video metadata and user comments.  
- **PostgreSQL** – Stores extracted data for further processing.  
- **Pandas** – Handles data transformation and storage.  
- **Requests & Schedule** – Handles API calls and automates data fetching.  

---  

## 📌 Features  

✅ **Extracts Reddit comments from specific subreddits**.  
✅ **Fetches YouTube video metadata & comments based on keywords**.  
✅ **Stores all data in a PostgreSQL database**.  
✅ **Implements API rate limiting to prevent request blocking**.  
✅ **Runs periodically using Python's `schedule` module**.  

---  

## 📂 Project Structure  

```
📁 Crawler/
│── Reddit_updated.py    # Scrapes Reddit comments using the API
│── Youtube_final_updated.py # Fetches YouTube video data & comments
│── subreddits.csv       # List of subreddits to scrape
│── Youtube_key.csv      # List of YouTube search keywords
│── README.md            # Project documentation
```  

---  

## 🚀 How It Works  

### **1️⃣ Setup API Credentials**  
Before running the crawler, update API credentials in the `Data_config.py` file:  

```python
REDDIT_API_CONFIG = {
    "client_id": "your-client-id",
    "client_secret": "your-client-secret",
    "username": "your-reddit-username",
    "password": "your-reddit-password"
}

API_KEYS = ["your-youtube-api-key1", "your-youtube-api-key2"]
```  

### **2️⃣ Prepare the Database**  
Ensure PostgreSQL is running and create the necessary tables:  

```sql
CREATE TABLE reddit_comments (
    id SERIAL PRIMARY KEY,
    subreddit TEXT,
    post_id TEXT,
    body TEXT,
    score INTEGER,
    created_utc TIMESTAMP,
    comment_id TEXT UNIQUE
);

CREATE TABLE yt_comments (
    ID SERIAL PRIMARY KEY,
    VIDEO_ID TEXT NOT NULL,
    VIDEO_TITLE TEXT NOT NULL,
    COMMENT_ID TEXT NOT NULL,
    COMMENT_TIME TEXT NOT NULL,
    COMMENT_TEXT TEXT NOT NULL
);
```  

### **3️⃣ Run the Reddit Scraper**  
```sh
python Reddit_updated.py
```  
This script:  
- Authenticates with Reddit.  
- Iterates through subreddits listed in `subreddits.csv`.  
- Fetches recent comments and stores them in PostgreSQL.  

### **4️⃣ Run the YouTube Scraper**  
```sh
python Youtube_final_updated.py
```  
This script:  
- Searches for videos using keywords from `Youtube_key.csv`.  
- Fetches comments from each video.  
- Stores the data in PostgreSQL.  

### **5️⃣ Automate the Scraping Process**  
```sh
python -m schedule
```  
This will run the crawler at **regular intervals** to fetch new data.  

---  

## 🔐 Data Considerations  

- **Rate Limits** → The script includes API rate limiting to prevent exceeding API request quotas.  
- **Data Duplication** → Uses PostgreSQL constraints to avoid inserting duplicate comments.  
- **Data Privacy** → Always adhere to Reddit & YouTube's API terms and conditions.  

---  

## 🔮 Future Enhancements  

🔹 **Parallel API Requests** → Improve efficiency by making concurrent API calls.  
🔹 **Support for More Sources** → Extend support to forums, blogs, and news websites.  
🔹 **Real-Time Crawling** → Upgrade to a streaming-based approach for live tracking.  

---  

## 📜 References  

- [Reddit API Documentation](https://www.reddit.com/dev/api/)  
- [YouTube API Documentation](https://developers.google.com/youtube/v3)  
- [PostgreSQL Official Site](https://www.postgresql.org/)  

---  

## 📧 Contact  

**Author:** Siddartha Reddy Boreddy  
📍 **SUNY Binghamton**  
✉️ **Email:** siddarthboreddy@xyz.com  

---  

### ⭐ If you find this project helpful, feel free to star the repository! 🚀  
