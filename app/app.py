from flask import Flask, render_template
import random
app = Flask(__name__)

images = [
  "https://media.tenor.com/CidTbb4N1mUAAAAM/chill-beach-life.gif",
  "https://media.tenor.com/f8-_uMdpE2sAAAAM/tenerife.gif",
  "https://media.tenor.com/4qU73Lkgy4YAAAAM/migration-safari-tours-nature.gif"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template('index.html', url=url)

if __name__ == "__main__":
   app.run(host="0.0.0.0")
