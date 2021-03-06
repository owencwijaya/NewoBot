from flask import Flask, render_template
from threading import Thread

app = Flask('')
wsgi_app = app.wsgi_app

@app.route('/')
def home():
    return "NewoBot is on and running"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()