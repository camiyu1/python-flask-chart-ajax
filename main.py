from app import app
from flask import jsonify, render_template
from random import sample

@app.route("/")
def index():
    return render_template("chart.html")


@app.route("/data")
def data():
    numDays = 7      # 7 days a week
    return jsonify({'result': sample(range(1, 10), numDays)})

if __name__ == "__main__":
    app.run(host="0.0.0.0")


