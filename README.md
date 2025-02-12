# 🌍 Social Media Data Science Sentiment & Hate Speech Analysis  

## 📖 Overview  

This project is a **multi-platform sentiment analysis and hate speech detection system** that collects, analyzes, and visualizes data from **Reddit and YouTube**. It is implemented using a **crawler, an analysis pipeline, and a web-based visualization tool** to extract insights from public discussions.  

---  

## 🛠 Technologies Used  

- **Python** – Core implementation language.  
- **Hadoop & MapReduce** – Large-scale data processing.  
- **Flask** – Web framework for visualization.  
- **PostgreSQL** – Database for storing processed data.  
- **Matplotlib & Pandas** – Data visualization.  
- **Bootstrap & HTML/CSS** – Frontend UI.  

---  

## 📌 Features  

✅ **Crawls Data from Reddit & YouTube**.  
✅ **Sentiment Analysis using NLP**.  
✅ **Hate Speech Detection API Integration**.  
✅ **Data Storage in PostgreSQL for Processing**.  
✅ **Web Dashboard for Insights & Visualization**.  

---  

## 📂 Project Structure  

```
📁 Main-Project/
│── 📁 Crawler/         # Scrapes data from Reddit & YouTube
│   │── Reddit_updated.py  
│   │── Youtube_final_updated.py  
│   │── subreddits.csv  
│   │── Youtube_key.csv  
│   └── README.md  
│  
│── 📁 Analysis/        # Processes collected data
│   │── an_all.py  
│   │── Analysis.yt.py  
│   │── plot.ipynb  
│   └── README.md  
│  
│── 📁 Web/             # Visualizes results
│   │── app.py  
│   │── templates/  
│   │── static/  
│   └── README.md  
│  
│── README.md          # Project documentation (this file)
```  

---  

## 🚀 How It Works  

### **1️⃣ Crawler (Data Collection)**  
- Scrapes comments from **Reddit & YouTube** based on specified topics.  
- Stores raw text data in **PostgreSQL**.  

### **2️⃣ Analysis (Data Processing)**  
- Cleans & processes the text data.  
- Performs **sentiment analysis & hate speech detection**.  
- Stores structured results for further use.  

### **3️⃣ Web Visualization (Insights & Reporting)**  
- Retrieves processed sentiment & hate speech data.  
- Provides **interactive charts & date-based filtering**.  
- Enables easy exploration of online discussions.  

---  

## 🏃 Running the Project  

### **1️⃣ Set Up Virtual Environment & Install Dependencies**  
```sh
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scriptsctivate      # Windows

pip install -r requirements.txt
```  

### **2️⃣ Run the Crawler**  
```sh
cd Crawler  
python Reddit_updated.py  
python Youtube_final_updated.py  
```  

### **3️⃣ Perform Analysis**  
```sh
cd Analysis  
python an_all.py  
python Analysis.yt.py  
```  

### **4️⃣ Start the Web Server**  
```sh
cd Web  
python app.py  
```  

### **5️⃣ View the Dashboard**  
Open in a web browser:  
```sh
http://127.0.0.1:5000/
```  

---  

## 🔮 Future Enhancements  

🔹 **Expand to More Platforms (Twitter, News, Forums)**.  
🔹 **Deploy Web App to AWS, GCP, or Heroku**.  
🔹 **Real-Time Streaming of Sentiment Analysis**.  
🔹 **Train a Custom AI Model for Hate Speech Detection**.  

---  

## 📜 References  

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [Reddit API](https://www.reddit.com/dev/api/)  
- [YouTube API](https://developers.google.com/youtube/v3)  
- [Matplotlib Visualization Guide](https://matplotlib.org/stable/)  

---  

## 📧 Contact  

**Author:** Siddartha Reddy Boreddy  
📍 **SUNY Binghamton**  
✉️ **Email:** sboreddy@binghamton.edu  

---  

### ⭐ If you find this project helpful, feel free to star the repository! 🚀 
