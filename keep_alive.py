from flask import Flask
From threading import Thread

app Flask(__name__)

@app.route('/')
def home():
  return "Bot is running!"
  
def run():
  app.run(host="0.0.0.0", port 8080)

def keep alive():
  t Thread(target-run)
  t.start()
