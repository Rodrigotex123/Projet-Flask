from flask import Flask, render_template
import requests
from random import shuffle

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html' )

@app.route('/video')
def index():
    donnees_obtenues=requests.get('https://api.dailymotion.com/videos?channel=news&limit=20')
    donnes_JSON=donnees_obtenues.json()
    videos = donnes_JSON['list'] 
    shuffle(videos)
    return render_template('index.html' , donees=videos[0:18])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 