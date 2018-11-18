def tachycardic_conditions(age, last_heart_rate):
    """ returns True or False

    This function determines if the patient is tachycardic based on
    their age and heart rate.

    It uses if statements to determine which category the user falls
    into based on their age, and if their heart rate is above the noted
    heart rate the statement returns True, otherwise it returns False.

    :param age: user's age
    :param last_heart_rate: heart rate value
    :type age: int
    :type last_heart_rate: int
    :return: True or False.
    :rtype: bool
    """

    if (1 / 365) <= age <= (2 / 365) and last_heart_rate > 159:
        return True
    if (2 / 365) < age <= (6 / 365) and last_heart_rate > 166:
        return True
    if (6 / 365) < age <= (28 / 365) and last_heart_rate > 182:
        return True
    if (28 / 365) < age <= (60 / 365) and last_heart_rate > 179:
        return True
    if (60 / 365) < age <= (180 / 365) and last_heart_rate > 186:
        return True
    if (180 / 365) < age <= (364 / 365) and last_heart_rate > 169:
        return True
    if (364 / 365) < age <= 2 and last_heart_rate > 151:
        return True
    if 2 < age <= 4 and last_heart_rate > 137:
        return True
    if 4 < age <= 7 and last_heart_rate > 133:
        return True
    if 7 < age <= 11 and last_heart_rate > 130:
        return True
    if 11 < age <= 15 and last_heart_rate > 119:
        return True
    if age > 15 and last_heart_rate > 100:
        return True
    else:
        return False
