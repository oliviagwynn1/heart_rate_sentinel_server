def test_tachycardic_conditions():
    """This function tests the tachycardic conditions function.

    The first line in the function is the input data being given into
    the test_tachycardic_conditions function. This is then tested in
    response to the result from the tachycardic_conditions function.
    """
    from tachy_conditions import tachycardic_conditions

    response = tachycardic_conditions(age=int(3), last_heart_rate=int(170))
    assert response
