from pymodm import MongoModel, fields


class Patient(MongoModel):

    patient_id = fields.IntegerField(primary_key=True)
    attending_email = fields.EmailField()
    user_age = fields.IntegerField()
    heart_rate_data = fields.ListField()

    REQUIRED_REQUEST_KEYS = [
        "user_id",
        "attending_email",
        "user_age"
    ]


class ValidationError(Exception):
    def __init__(self, exception):
        self.exception = exception


def validate_patient(req):
    """This function validates the patient data.

    This functions uses a for loop to ensure that all patient data is
    inputted correctly. It ensures that the request data contains the
    keys in the required request keys list. If a key is not in the
    request input a Validation Error is raised.

    :param req: requests
    """
    p = Patient()
    for key in p.REQUIRED_REQUEST_KEYS:
        if key not in req.keys():
            raise ValidationError(
                "Key '{0}' not present in request".format(key))
