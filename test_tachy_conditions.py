
def test_tachycardic_conditions():
    from tachy_conditions import tachycardic_conditions

    response = tachycardic_conditions(user_id=int(2), age=int(3), last_heart_rate=int(145))
    assert response == "Patient {} is Tachycardic.".format(2)



