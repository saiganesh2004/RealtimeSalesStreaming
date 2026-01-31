# RealtimeSalesStreaming

## Real-Time Sales Monitoring Dashboard

A production-style **real-time data streaming and analytics dashboard** built using Python, Streamlit, and Redis Streams. This project simulates live sales data ingestion, processes streaming events using a producer–consumer architecture, and visualizes key business KPIs in real time.

---

## 🚀 Key Features

* Real-time sales data streaming using **Redis Streams**
* Interactive **Streamlit dashboard** for live monitoring
* KPI tracking: total sales, transaction count, hourly trends
* Alert generation for abnormal sales spikes
* Producer–consumer architecture
* Localhost and Docker-ready deployment

---

## 🏗️ Architecture Overview

```
Producer (Python)
   ↓
Redis Streams
   ↓
Consumer / Processor
   ↓
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (Dashboard & Visualization)
* **Redis Streams** (Real-time data streaming)
* **Pandas & NumPy** (Data processing)
* **Docker** (Containerization – optional)

---

## 📂 Project Structure

```
RealtimeSalesStreaming/
│── app.py                # Streamlit dashboard
│── producer.py           # Sales data producer
│── alert_history.csv     # Generated alerts log
│── randomdata.ipynb      # Data simulation notebook
│── redisdata.ipynb       # Redis testing notebook
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/saiganesh2004/RealtimeSalesStreaming.git
cd RealtimeSalesStreaming
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Start Redis (Localhost)

```
redis-server
```

### 4️⃣ Run the Producer

```
python producer.py
```

### 5️⃣ Run the Dashboard

```
streamlit run app.py
```

---

## 🐳 Run with Docker (Optional)

```
docker build -t realtime-sales .
docker run -p 8501:8501 realtime-sales
```

---

## 📊 Use Cases

* Real-time sales analytics
* Streaming data pipeline demonstration
* Monitoring transaction spikes
* Entry-level data engineering & analytics project

---

## 🎯 Learning Outcomes

* Hands-on experience with **streaming data systems**
* Understanding producer–consumer pipelines
* Real-time dashboard development
* Redis Streams fundamentals
* Docker-based deployment basics

---

## 📌 Future Enhancements

* Cloud deployment (AWS / GCP)
* Kafka-based streaming support
* Authentication & role-based dashboards
* Persistent database integration

---

## 👤 Author

**Sai Ganesh**
Aspiring Data Analyst / Data Engineer

---

⭐ If you find this project useful, consider starring the repository!
