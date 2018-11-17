from flask import Flask, jsonify
from pymodm import connect
from database import Patient
from tachy_conditions import tachycardic_conditions

app = Flask(__name__)


@app.route("/api/status/<user_id>", methods=["GET"])
def is_tachycardic(user_id):
    user_id = int(user_id)
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    user = Patient.objects.raw({"_id": user_id}).first()
    age = user.user_age
    last_heart_rate = user.heart_rate_data[-1]["hr"]

    # tachycardic_conditions(user_id, age, last_heart_rate)
    return tachycardic_conditions(user_id, age, last_heart_rate)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)


