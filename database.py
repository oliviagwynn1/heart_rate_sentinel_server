from pymodm import MongoModel, fields

class Patient(MongoModel):

    user_id = fields.IntegerField(primary_key=True)
    attending_email = fields.EmailField()
    user_age = fields.IntegerField()
    heart_rate = fields.ListField()
    time_stamp = fields.ListField(field =fields.DateTimeField)

