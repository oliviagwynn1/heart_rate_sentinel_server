from database import Patient


def list_heart_rates():
    for user in Patient:
        print(user.user_id)
        print(user.heart_rate)

