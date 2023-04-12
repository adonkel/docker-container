from flask import Flask, render_template
import os
import random

app = Flask(__name__)

#list of images
images = [
    "https://media.tenor.com/CZ6eoFdCszMAAAAC/simpson-homer.gif",
    "https://media.tenor.com/zzDQG5XmVYIAAAAd/abe-simpson-the-simpsons.gif",
    "https://media.tenor.com/ht_m9ppITb0AAAAd/the-simpsons-mr-burns.gif",
    "https://media.tenor.com/IRfP_JuajbIAAAAC/ralph-the-simpsons.gif",
]

@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))