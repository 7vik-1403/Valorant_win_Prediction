# 🎮 Valorant Live Match Prediction System

A real-time machine learning system that predicts which team (A or B) is currently winning in a Valorant round based on in-game state.

---

## 🚀 Features

* 🔥 Real-time prediction using ML model
* ⚡ FastAPI backend for inference
* 🗄️ PostgreSQL database for live game data
* 📊 Streamlit dashboard with live graphs
* 🔁 Continuous data pipeline simulation

---

## 🧠 Tech Stack

* **Backend:** FastAPI
* **ML Model:** Scikit-learn (RandomForest)
* **Database:** PostgreSQL
* **Dashboard:** Streamlit
* **Deployment:** GCP / Render

---

## 🏗️ System Architecture

```
Game Data → PostgreSQL → FastAPI → ML Model → Streamlit Dashboard
```

---

## 📂 Project Structure

```
.
├── main.py              # FastAPI app
├── pipeline.py          # Preprocessing logic
├── valorant_.pkl        # Trained ML model
├── dashboard.py         # Streamlit UI
├── insert_data.py       # Data simulation script
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone repo

```
git clone https://github.com/7vik-1403
/valorant-ml.git
cd valorant-ml
```

---

### 2️⃣ Create virtual environment

```
python -m venv .venv
.\.venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Setup PostgreSQL

Create database:

```
CREATE DATABASE valorant_db;
```

Create table:

```
CREATE TABLE round_data (
    id SERIAL PRIMARY KEY,
    timestamp VARCHAR(10),
    attack_side VARCHAR(1),

    A_rifle_players INT,
    B_rifle_players INT,
    A_pistol_players INT,
    B_pistol_players INT,

    A_half_shield INT,
    B_half_shield INT,
    A_full_shield INT,
    B_full_shield INT,
    A_regen_shield INT,
    B_regen_shield INT,

    players_alive_A INT,
    players_alive_B INT,

    spike_planted INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

### 5️⃣ Run data generator

```
python insert_data.py
```

---

### 6️⃣ Run FastAPI

```
uvicorn main:app --reload
```

API available at:

```
http://127.0.0.1:8000/docs
```

---

### 7️⃣ Run Dashboard

```
python -m streamlit run dashboard.py
```

---

## 📡 API Endpoints

### GET `/`

Health check

### GET `/live`

Returns latest game state + prediction

---

## 📊 Example Response

```json
{
  "current_winning": "A",
  "data": {
    "timestamp": "01:20",
    "players_alive_A": 3,
    "players_alive_B": 2
  }
}
```

---

## 🧪 Model Features

* Time (seconds)
* Rifle players (A & B)
* Pistol players (A & B)
* Shield types
* Players alive
* Attack side
* Spike planted

---

## 🌐 Deployment

### GCP (Recommended)

* Cloud Run → FastAPI
* Cloud SQL → PostgreSQL
* Streamlit Cloud → UI

---

## 🚀 Future Improvements

* 📈 Win probability prediction
* 🎯 Round-level analytics
* ⚡ WebSocket real-time updates
* 🧠 Advanced feature engineering
* 🌐 Full production deployment

---

## 👨‍💻 Author

Satvik Deshmukh 

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!


