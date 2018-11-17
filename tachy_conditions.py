def tachycardic_conditions(user_id, age, last_heart_rate):
    from flask import jsonify
    message1 = "Patient {} is Tachycardic.".format(user_id)
    message2 = "Patient {} is not Tachycardic.".format(user_id)

    if (1/365) <= age <= (2/365) and last_heart_rate > 159:
        return jsonify(message1)
    if (2/365) < age <= (6/365) and last_heart_rate > 166:
        return jsonify(message1)
    if (6/365) < age <= (28/365) and last_heart_rate > 182:
        return jsonify(message1)
    if (28/365) < age <= (60/365) and last_heart_rate > 179:
        return jsonify(message1)
    if (60/365) < age <= (180/365) and last_heart_rate > 186:
        return jsonify(message1)
    if (180/365) < age <= (364/365) and last_heart_rate > 169:
        return jsonify(message1)
    if (364/365) < age <= 2 and last_heart_rate > 151:
        return jsonify(message1)
    if 2 < age <= 4 and last_heart_rate > 137:
        return jsonify(message1)
    if 4 < age <= 7 and last_heart_rate > 133:
        return jsonify(message1)
    if 7 < age <= 11 and last_heart_rate > 130:
        return jsonify(message1)
    if 11 < age <= 15 and last_heart_rate > 119:
        return jsonify(message1)
    if age > 15 and last_heart_rate > 100:
        return jsonify(message1)
    else:
        return jsonify(message2)
