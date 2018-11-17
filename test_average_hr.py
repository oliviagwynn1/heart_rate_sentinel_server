def test_average_hr():
    from avg_heart_rate import average_hr

    response = average_hr(heart_rates=[190, 100, 170])
    assert response == str(float((190+100+170)/3))
