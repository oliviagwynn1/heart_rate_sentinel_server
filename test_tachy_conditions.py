
def test_tachycardic_conditions():
    from tachy_conditions import tachycardic_conditions

    response = tachycardic_conditions(user_id=2, age=3, last_heart_rate=[145])
    assert response == "Patient 2 is Tachycardic."



