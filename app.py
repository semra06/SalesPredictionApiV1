from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        "message": "Merhaba Pair9,SalesPredictionApiV1 uygulaması  Docker'da çalışıyor!",
        "versiyon": "v1.0",
        "durum": "Her şey yolunda ✅"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

