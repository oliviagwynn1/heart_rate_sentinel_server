from flask import Flask, jsonify, request
from pymodm import connect
from database import Patient
from database import ValidationError
from database import validate_patient


app = Flask(__name__)


@app.route("/")
def server_on():
    return "hello!"


@app.route("/api/new_patient", methods=["POST"])
def add_patient():
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json() # parses the POST request body as JSON

    try:
        validate_patient(r)
    except ValidationError as inst:
        return jsonify({"message": inst.exception}), 500

    p = Patient(user_id=r["user_id"], attending_email=r["attending_email"], user_age=r["user_age"])
    p.save()

    result = {
        "message": "Added patient {0} successfully to the patient list".format(request.json["user_id"])
    }

    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def add_heart_rate():
    import time

    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json()

    t = time.time()

    id_user = Patient.objects.raw({"_id": r["user_id"]})
    data = [{"hr": hr, "time": t} for hr in r["heart_rate"]]
    id_user.update(
        {"$push": {"heart_rate_data": {"$each": data}}}
    )

    result = {
        "message": "Added patient {0} heart rate successfully to the patient list".format(request.json["user_id"])
    }

    return jsonify(result)


@app.route("/api/heart_rate/<user_id>", methods=["GET"])
def list_heart_rates(user_id):
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    user_id = int(user_id)
    user = Patient.objects.raw({"_id": user_id}).first()

    return jsonify(user.heart_rate_data)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)


#   r2 = requests.post("http://127.0.0.1:5000/api/new_patient", json={"user_id": 1,"attending_email": "olivia.gwynn@duke.edu","user_age": 21})
