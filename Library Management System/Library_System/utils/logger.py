from datetime import datetime

def log(message):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{time_stamp}] {message}"
    print(log_message)

    # Also write to a file
    with open("library.log", "a") as f:
        f.write(log_message + "\n")
