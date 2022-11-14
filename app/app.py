from flask import Flask, render_template
import random
app = Flask(__name__)

images = [
  "https://media.tenor.com/CidTbb4N1mUAAAAM/chill-beach-life.gif",
  "https://media0.giphy.com/media/WQxjLKcDsS5aEY60vX/200w.webp?cid=ecf05e47eauitp5faaen2z0lwcr6fdyns034p2qnofzzpdxq&rid=200w.webp&ct=g",
  "https://media0.giphy.com/media/gKSo8pul2vHIFJCwBz/200w.webp?cid=ecf05e47eauitp5faaen2z0lwcr6fdyns034p2qnofzzpdxq&rid=200w.webp&ct=g"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
   app.run(host="0.0.0.0")
