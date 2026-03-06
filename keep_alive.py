from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    # Render or Replit will set PORT; default to 8080 if not set
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    # Run the Flask server in a separate thread
    t = Thread(target=run)
    t.start()