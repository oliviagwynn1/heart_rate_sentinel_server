def avg_hr_specified(new_time_since, heart_rate_values):
    """returns avg_heart_rate

    This function calculates the average heart rate after a specified
    time.

    This function uses a for loop to sum the values of all heart rates,
    while utilising a count variable to determine how many heart rate
    values were added. The heart values are only added if it's
    corresponding time stamp is greater than the specified time. The
    average is then determined from dividing the sum of the heart rates
    by the count number.

    :param new_time_since: time stamp
    :param heart_rate_values: heart rate values
    :type new_time_since: float
    :type heart_rate_values: list
    :return: average heart rate
    :rtype: str
    """

    heart_rate_total = 0
    count = 0

    for data in heart_rate_values:
        if data["time"] >= new_time_since:
            heart_rate_total += data["hr"]
            count += 1

    avg_heart_rate = str(float(heart_rate_total / count))

    return avg_heart_rate
