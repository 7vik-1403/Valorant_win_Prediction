
import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Valorant Live Dashboard", layout="wide")

st.title("🎮 Valorant Live Match Dashboard")

# store history
if "history" not in st.session_state:
    st.session_state.history = []

placeholder = st.empty()

while True:
    try:
        res = requests.get("http://127.0.0.1:8000/live").json()

        data = res["data"]
        prediction = res["current_winning"]

        # add to history
        st.session_state.history.append({
            "time": data["timestamp"],
            "players_A": data["players_alive_A"],
            "players_B": data["players_alive_B"],
            "rifle_A": data["A_rifle_players"],
            "rifle_B": data["B_rifle_players"],
            "prediction": prediction
        })

        df = pd.DataFrame(st.session_state.history)

        with placeholder.container():

            # 🔥 Current prediction
            st.subheader(f"🏆 Current Winning: {prediction}")

            col1, col2 = st.columns(2)

            # 👥 Players alive graph
            with col1:
                st.subheader("Players Alive")
                st.line_chart(df[["players_A", "players_B"]])

            # 🔫 Rifle advantage graph
            with col2:
                st.subheader("Rifle Advantage")
                st.line_chart(df[["rifle_A", "rifle_B"]])

           
            st.subheader("Latest Game State")
            st.json(data)

        time.sleep(2)

    except Exception as e:
        st.error(f"Error: {e}")
        time.sleep(2)

