def preprocess(data):
    m, s = data["timestamp"].split(":")
    time_sec = int(m) * 60 + int(s)
    attack_side = 0 if data["attack_side"] == "A" else 1
    return time_sec, attack_side
