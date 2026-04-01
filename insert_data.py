
import psycopg2
import random
import time

conn = psycopg2.connect(
    host="localhost",
    database="valorant_db",
    user="postgres",
    password="@7vik123"
)

cursor = conn.cursor()

while True:
    data = {
        "timestamp": f"{random.randint(0,1):02}:{random.randint(0,59):02}",
        "attack_side": random.choice(["A", "B"]),

        "A_rifle_players": random.randint(0,5),
        "B_rifle_players": random.randint(0,5),
        "A_pistol_players": random.randint(0,5),
        "B_pistol_players": random.randint(0,5),

        "A_half_shield": random.randint(0,5),
        "B_half_shield": random.randint(0,5),
        "A_full_shield": random.randint(0,5),
        "B_full_shield": random.randint(0,5),
        "A_regen_shield": random.randint(0,5),
        "B_regen_shield": random.randint(0,5),

        "players_alive_A": random.randint(0,5),
        "players_alive_B": random.randint(0,5),

        "spike_planted": random.randint(0,1)
    }

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

    values = tuple(data.values())

    cursor.execute(query, values)
    conn.commit()

    print("Inserted:", data)

    time.sleep(2)

