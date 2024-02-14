from flask import Flask

app1 = Flask(__name__)


@app1.route("/")
def home():
    return "Hello, this is App 1!"


if __name__ == "__main__":
    app1.run(host="0.0.0.0", port=5000)
