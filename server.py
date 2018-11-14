from flask import Flask, jsonify, request
from pymodm import connect
from database import Patient

app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def add_patient():
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json() # parses the POST request body as JSON

    try:
        validate_new_patient(r)
    except ValidationError as inst:
        return jsonify({"message": inst.exception}), 500

    p = Patient(user_id="1", attending_email="olivia.gwynn@duke.edu", user_age="21")
    p.save()

    result = {
        "message": "Added patient {0} successfully to the patient list".format(request.json["user_id"])
    }

    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def add_heart_rate():
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json()

    id_user = Patient.objects.raw({"_id": r["user_id"]})
    id_user.update(
        {"$push": {"heart_rate": r["heart_rate"]}}
    )

    result = {
        "message": "Added patient {0} heart rate successfully to the patient list".format(request.json["user_id"])
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)

#   r2 = requests.post("http://127.0.0.1:5000/add_patient", json={"user_id": 2,"attending_email": "olivia.gwynn@duke.edu","user_age": 21,"heart_rate": [100, 90, 110]})
