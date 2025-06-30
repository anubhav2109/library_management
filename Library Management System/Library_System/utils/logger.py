from datetime import datetime

def log(message):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{time_stamp}] {message}")
