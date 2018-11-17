from pymodm import MongoModel, fields


class Patient(MongoModel):

    user_id = fields.IntegerField(primary_key=True)
    attending_email = fields.EmailField()
    user_age = fields.IntegerField()
    heart_rate = fields.ListField()
#    time_stamp = fields.ListField(field=fields.DateTimeField)

    REQUIRED_REQUEST_KEYS = [
        "user_id",
        "attending_email",
        "user_age"
    ]


class ValidationError(Exception):
    def __init__(self, exception):
        self.exception = exception


def validate_patient(req):
    p = Patient()
    for key in p.REQUIRED_REQUEST_KEYS:
        if key not in req.keys():
            raise ValidationError("Key '{0}' not present in request".format(key))
