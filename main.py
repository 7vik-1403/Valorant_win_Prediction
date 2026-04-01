
from pyexpat import features
from fastapi import FastAPI 

import os
import psycopg2
conn = psycopg2.connect( os.getenv("DATABASE_URL"), sslmode="require" ) 
cursor = conn.cursor()
import joblib
from pipeline import preprocess
app = FastAPI()
model_ = joblib.load('valorant_.pkl')
from pydantic import BaseModel
class GameState(BaseModel):
    timestamp: str
    attack_side: str
    A_rifle_players: int
    B_rifle_players: int
    A_pistol_players: int
    B_pistol_players: int
    A_half_shield: int
    B_half_shield: int
    A_full_shield: int
    B_full_shield: int
    A_regen_shield: int
    B_regen_shield: int
    players_alive_A: int
    players_alive_B: int
    spike_planted: int

@app.get("/")
def home():
    return {"message": "Hello World"}
@app.post("/predict")
def predict(data: GameState):  
    data_dict = data.dict()  
    time_sec , attack_side = preprocess(data_dict)
    features = [[ int(time_sec), int(data.A_rifle_players), int(data.B_rifle_players), int(data.A_pistol_players), int(data.B_pistol_players), int(data.A_half_shield), int(data.B_half_shield), int(data.A_full_shield), int(data.B_full_shield), int(data.A_regen_shield), int(data.B_regen_shield), int(data.players_alive_A), int(data.players_alive_B), int(attack_side), int(data.spike_planted) ]]
    prediction = model_.predict(features)
    return {"current_winning": "A" if prediction == 0 else "B"}

def insert_data(data):
    query = """
    INSERT INTO round_data (
        timestamp, attack_side,
        A_rifle_players, B_rifle_players,
        A_pistol_players, B_pistol_players,
        A_half_shield, B_half_shield,
        A_full_shield, B_full_shield,
        A_regen_shield, B_regen_shield,
        players_alive_A, players_alive_B,
        spike_planted
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["timestamp"], data["attack_side"],
        data["A_rifle_players"], data["B_rifle_players"],
        data["A_pistol_players"], data["B_pistol_players"],
        data["A_half_shield"], data["B_half_shield"],
        data["A_full_shield"], data["B_full_shield"],
        data["A_regen_shield"], data["B_regen_shield"],
        data["players_alive_A"], data["players_alive_B"],
        data["spike_planted"]
    )

    cursor.execute(query, values)
    conn.commit()
def get_latest():
    cursor.execute("""
        SELECT * FROM round_data
        ORDER BY id DESC
        LIMIT 1
    """)
    
    row = cursor.fetchone()

    if row:
        return {
            "timestamp": row[1],
            "attack_side": row[2],
            "A_rifle_players": row[3],
            "B_rifle_players": row[4],
            "A_pistol_players": row[5],
            "B_pistol_players": row[6],
            "A_half_shield": row[7],
            "B_half_shield": row[8],
            "A_full_shield": row[9],
            "B_full_shield": row[10],
            "A_regen_shield": row[11],
            "B_regen_shield": row[12],
            "players_alive_A": row[13],
            "players_alive_B": row[14],
            "spike_planted": row[15]
        }

@app.get("/live")
def live_prediction():
    data = get_latest()

    time_sec, attack_side = preprocess(data)

    features = [[
        time_sec,
        data["A_rifle_players"],
        data["B_rifle_players"],
        data["A_pistol_players"],
        data["B_pistol_players"],
        data["A_half_shield"],
        data["B_half_shield"],
        data["A_full_shield"],
        data["B_full_shield"],
        data["A_regen_shield"],
        data["B_regen_shield"],
        data["players_alive_A"],
        data["players_alive_B"],
        attack_side,
        data["spike_planted"]
    ]]

    prediction = model_.predict(features)[0]

    return {
        "current_winning": prediction,
        "data": data
    }
