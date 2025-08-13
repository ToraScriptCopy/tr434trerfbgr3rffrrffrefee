from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1>Сайт работает!</h1><p>Это главная страница.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
