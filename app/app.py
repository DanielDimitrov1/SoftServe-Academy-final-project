from flask import Flask, render_template
import random
app = Flask(__name__)

# list of cat images
images = [
  "https://media2.giphy.com/media/jTMxfXzAohYnkiTZlg/200w.webp?cid=ecf05e47h1ke9bsyx9hp1f1f98yg7x8gucxracvpq7jc1q4g&rid=200w.webp&ct=g"
]
@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
   app.run(host="0.0.0.0")
