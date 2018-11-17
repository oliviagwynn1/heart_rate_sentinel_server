def average_hr(heart_rates):
    number_values = 0
    sum_hr = 0
    for values in heart_rates:
        number_values += 1
        sum_hr += values

    hr_avg = sum_hr/number_values

    return str(float(hr_avg))
