

def avg_hr_specified(new_time_since, heart_rate_values):

    heart_rate_total = 0
    count = 0

    for data in heart_rate_values:
        if data["time"] >= new_time_since:
            heart_rate_total += data["hr"]
            count += 1
    avg_heart_rate = str(float(heart_rate_total/count))

    return avg_heart_rate
