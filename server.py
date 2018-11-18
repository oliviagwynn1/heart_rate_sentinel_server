# import logging
# from logging import config
from flask import Flask, jsonify, request
from pymodm import connect
from database import Patient
from database import ValidationError
from database import validate_patient



app = Flask(__name__)


@app.route("/api/new_patient", methods=["POST"])
def add_patient():
    """This function creates a new patient.

    This function connects to the Mongo database, and posts data to the
    database. It uses a try statement to validate the data being parsed
    into the function. If the data is not valid then a Validation Error
    is returned.

    The function also sets up a model for the data being parsed in and
    saves it to the Patient class. It returns a message to confirm the
    addition of the new patient to the database.

    :return: message
    :rtype: str
    """

    # logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json()  # parses the POST request body as JSON

    try:
        validate_patient(r)
    except ValidationError as inst:
        return jsonify({"message": inst.exception}), 500

    p = Patient(
        user_id=r["user_id"],
        attending_email=r["attending_email"],
        user_age=r["user_age"])
    p.save()

    result = {
        "message": "Added patient {0} successfully to the patient list".format(
            request.json["user_id"])}
    # logging.info(result)

    return jsonify(result)


@app.route("/api/heart_rate", methods=["POST"])
def add_heart_rate():
    """This function adds heart rate data to existing patient.

    This function connects to the Mongo database, and posts data to the
    database. It requires the 'time' package that generates a time stamp
    when the new heart rate data is parsed into the function.

    The id_user finds the patient with the given user_id and their
    corresponding data. The 'data' variable creates a list containing
    dictionaries to store the heart rate values and corresponding time
    values. These are labelled hr and time, respectively. The '$push'
    string adds the new heart rate data to the patient without
    overwriting any previous data.

    The function returns a message to confirm the addition of the new
    heart rate to the patient in the database.

    :return: message
    :rtype: str
    """

    import time

    # logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json()

    t = time.time()

    id_user = Patient.objects.raw({"_id": r["user_id"]})
    data = [{"hr": hr, "time": t} for hr in r["heart_rate"]]
    id_user.update(
        {"$push": {"heart_rate_data": {"$each": data}}}
    )

    result = {
        "message": "Added patient {0} heart rate successfully to the patient list".format(
            request.json["user_id"])}
    # logging.info(result)

    return jsonify(result)


@app.route("/api/heart_rate/<user_id>", methods=["GET"])
def list_heart_rates(user_id):
    """This function creates a new patient.

    This function connects to the Mongo database, and gets data from
    the database. The input user_id is converted from a string to int,
    and used to locate the patient in question.

    The function returns a list of all the heart rates associated with
    the patient.

    :param user_id: user id
    :type user_id: str
    :return: heart rates
    :rtype: list
    """

    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    user_id = int(user_id)
    user = Patient.objects.raw({"_id": user_id}).first()

    return jsonify(user.heart_rate_data)


@app.route("/api/status/<user_id>", methods=["GET"])
def is_tachycardic(user_id):
    """This function checks to see if a patient is tachycardic.

    This function connects to the Mongo database, and gets data from
    the database. The input user_id is converted from a string to int,
    and used to locate the patient in question.

    This function finds the age of the user, their last inputted heart
    rate value, as well as their email. This information is parsed into
    another function called 'tachycardic_conditions' to determine if the
    patient is tachycardic. If the patient is tachycardic, and email is
    sent to them using Sendgrid. It returns a message stating the patient
    status.

    :param user_id: user id
    :type user_id: str
    :return: message
    :rtype: str
    """

    from tachy_conditions import tachycardic_conditions
    from sendgrid_email import send_email

    # logging.config.fileConfig('logger_config.ini', disable_existing_loggers=False)
    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    user_id = int(user_id)

    user = Patient.objects.raw({"_id": user_id}).first()
    age = user.user_age
    last_heart_rate = user.heart_rate_data[-1]["hr"]
    attending_email = user.attending_email

    result = tachycardic_conditions(age, last_heart_rate)
    if result is True:
        send_email(attending_email)
        # logging.info("Patient {} is Tachycardic.".format(user_id))
        return jsonify("Patient {} is Tachycardic.".format(user_id))
    else:
        # logging.info("Patient {} is not Tachycardic.".format(user_id))
        return jsonify("Patient {} is not Tachycardic.".format(user_id))


@app.route("/api/heart_rate/average/<user_id>", methods=["GET"])
def avg_hr(user_id):
    """This function determines the average heart rate.

    This function connects to the Mongo database, and gets data from
    the database. The input user_id is converted from a string to int,
    and used to locate the patient in question.

    This function creates an empty list of heart rates, and utilizes a
    for loop. The for loop appends all the heart rate values from the
    list of dictionaries that contains the heart rate values and time
    stamps. This heart rate list is then parsed into a function called
    'average_hr' that calculates the average heart rate over all values.

    :param user_id: user id
    :type user_id: str
    :return: message
    :rtype: str
    """
    from avg_heart_rate import average_hr

    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    user_id = int(user_id)

    user = Patient.objects.raw({"_id": user_id}).first()
    heart_rates = []

    for data in user.heart_rate_data:
        heart_rates.append(data["hr"])

    return jsonify(str(float(average_hr(heart_rates))))


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def interval_avg():
    """This function determines the average heart rate after a
    specified time.

   This function connects to the Mongo database, and uses data from
   the database. This function uses a request.get to parse in the
   information sent from the client. The user_id is determined from
   the request, and locates the user and associated data. The specified
   time is also determined from the request information.

   The function stores the heart rate data and corresponding time stamps
   into a list, as well as converting the given time stamp from UTC to
   unix form. This data is then parsed into another function called
   'avg_hr_specified', that determines the average heart rate since the
   given time.

   :return: message
   :rtype: str
   """

    from avg_hr_spec import avg_hr_specified
    import datetime

    connect("mongodb://oliviagwynn1:GODUKE10@ds157503.mlab.com:57503/bme590")
    r = request.get_json()

    user = Patient.objects.raw({"_id": r["user_id"]}).first()
    time_since = r["heart_rate_data_since"]
    heart_rate_values = user.heart_rate_data
    new_time_since = datetime.datetime.fromisoformat(time_since).timestamp()

    return jsonify(avg_hr_specified(new_time_since, heart_rate_values))


if __name__ == "__main__":
    # app.run(host="vcm-7433.vm.duke.edu", port=5000)
    app.run(host="127.0.0.1", port=5002)