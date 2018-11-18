def average_hr(heart_rates):
    """returns hr_avg

    This function calculates the average heart rate over all values.

    This function uses a for loop to sum the values of all heart rates,
    while utilising a count variable to determine how many heart rate
    values were added. The average is then determined from dividing the
    sum of the heart rates by the count number.

    :param heart_rates: heart rate values
    :type heart_rates: list
    :return: average heart rate
    :rtype: str
    """

    number_values = 0
    sum_hr = 0
    for values in heart_rates:
        number_values += 1
        sum_hr += values

    hr_avg = sum_hr / number_values

    return hr_avg
