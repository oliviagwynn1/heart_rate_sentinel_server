def test_average_hr():
    """This function tests the average heart rate function.

    The first line in the function is the input data being given into
    the test_average_hr function. This is then tested in response to the
    result from the average_hr function.
    """

    from avg_heart_rate import average_hr

    response = average_hr(heart_rates=[190, 100, 170])
    assert response == (190 + 100 + 170) / 3
