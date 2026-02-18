from datetime import datetime

def log(event):
    with open("logs/events.log", "a") as f:
        f.write(f"{datetime.now()} - {event}\n")
