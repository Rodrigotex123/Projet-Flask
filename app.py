from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def index():
    donnees_obtenues=requests.get('https://api.dailymotion.com/videos?channel=sport&limit=10')
    donnes_JSON=donnees_obtenues.json()
    print(donnes_JSON)
    return render_template('index.html' , donees=donnes_JSON['list'])

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 