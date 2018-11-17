def test_avg_hr_specified():
    from avg_hr_spec import avg_hr_specified

    response = avg_hr_specified(new_time_since=123456, heart_rate_values=[{"hr": 130, "time": 123450},
                                                                          {"hr": 140, "time": 123460},
                                                                          {"hr": 60, "time": 123490}]
                                )

    assert response == str(float((140+60)/2))
