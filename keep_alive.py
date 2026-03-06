from flask import Flask
import requests
import time
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"
def self_ping():
    url = os.environ.get("RENDER_EXTERNAL_URL", "http://localhost:8080")
    while True:
        time.sleep(240)
        try:
            requests.get(url)
        except:
            pass

def run():
    # Render or Replit will set PORT; default to 8080 if not set
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    # Run the Flask server in a separate thread
    t = Thread(target=run)
    t.daemon = True
    t.start()

    p = Thread(target=self_ping)
    p.daemon = True
    p.start()