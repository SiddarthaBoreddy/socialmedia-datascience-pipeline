# 🌐 Sentiment Analysis & Hate Speech Detection Web Dashboard  

## 📖 Overview  

This module implements a **Flask-based web dashboard** to **visualize sentiment analysis and hate speech detection results**. The frontend provides interactive visualizations and allows users to explore sentiment trends and hate speech insights over time.  

This dashboard is part of a larger **3-part project**, where:  
- **Part 1 (Crawler)** → Fetches data from Reddit & YouTube.  
- **Part 2 (Analysis)** → Processes and analyzes sentiment and hate speech.  
- **Part 3 (Web Visualization)** → Presents insights on a web page.  

---  

## 🛠 Technologies Used  

- **Flask (Python Web Framework)** – Handles backend requests.  
- **HTML, CSS, Bootstrap** – Frontend design and styling.  
- **Jinja2 (Flask Templates)** – Dynamically renders analysis results.  
- **Matplotlib & Pandas** – Generates plots for visualization.  
- **PostgreSQL** – Stores processed sentiment and hate speech analysis results.  

---  

## 📌 Features  

✅ **Interactive Dashboard** – Displays visual insights for sentiment & hate speech analysis.  
✅ **Dynamic Graphs** – Visualizes sentiment trends, comment volume, and hate speech detection.  
✅ **User Input Options** – Allows filtering by **start & end dates**.  
✅ **Bootstrap UI** – Modern, responsive, and user-friendly interface.  
✅ **Flask Backend** – Efficient data retrieval and dynamic content rendering.  

---  

## 📂 Project Structure  

```
📁 Web-Dashboard/
│── app.py            # Flask backend for rendering data
│── templates/
│   └── index.html    # Frontend for interactive dashboard
│── static/           # Contains CSS, JavaScript, and images
│── README.md         # Project documentation
```  

---  

## 🚀 How It Works  

### **1️⃣ Set Up Virtual Environment & Install Dependencies**  
```sh
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scriptsctivate      # For Windows

pip install -r requirements.txt
```  

### **2️⃣ Set Up PostgreSQL Database**  
Ensure the sentiment analysis results are stored in a PostgreSQL table:  

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

### **3️⃣ Run Flask Server**  
```sh
python app.py
```  

This starts the **Flask web application**. By default, it runs on `http://127.0.0.1:5000/`.

### **4️⃣ Access the Dashboard**  
Open a web browser and navigate to:  
```sh
http://127.0.0.1:5000/
```  

---  

## 🎨 Dashboard Sections  

- **📊 Data Trends** – Visualizes comment volume over time.  
- **📈 Sentiment Analysis** – Displays positive, negative, and neutral sentiment trends.  
- **🚨 Hate Speech Detection** – Shows flagged comments and confidence levels.  
- **📅 Date-Based Filtering** – Users can select custom date ranges to refine insights.  

---  

## 🔐 Data Considerations  

- **Real-Time Updates** → Refreshing the dashboard fetches the latest data from the database.  
- **Scalability** → The Flask backend can be expanded to handle larger datasets.  
- **Security** → Ensure proper input validation to prevent **SQL injection** attacks.  

---  

## 🔮 Future Enhancements  

🔹 **Deploy on Cloud (AWS, Heroku, GCP)** for public access.  
🔹 **Add User Authentication** to restrict data access.  
🔹 **Enhance UI with JavaScript & Chart.js for interactive visualizations.**  
🔹 **Integrate AI-based Sentiment Predictions** for better accuracy.  

---  

## 📜 References  

- [Flask Documentation](https://flask.palletsprojects.com/)  
- [Bootstrap Framework](https://getbootstrap.com/)  
- [Matplotlib & Pandas](https://matplotlib.org/stable/)  

---  

## 📧 Contact  

**Author:** Siddartha Reddy Boreddy  
📍 **SUNY Binghamton**  
✉️ **Email:** sboreddy@binghamton.edu  

---  

### ⭐ If you find this project helpful, feel free to star the repository! 🚀  
