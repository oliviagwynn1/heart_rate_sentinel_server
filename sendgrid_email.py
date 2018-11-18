from sendgrid.helpers.mail import *


def send_email(attending_email):
    """This function sends an email to a patient.

    The function utilizes the SendGrid delivery service to send an email
    to the attending_email. The contents and subject of the email are
    specified in the subject and content variables.

    :param attending_email:
    :type attending_email: str
    """

    import sendgrid
    import os

    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

    from_email = Email("olivia.gwynn@duke.edu")
    to_email = Email(attending_email)
    subject = "Tachycardic Results"
    content = Content("Unfortunately you have Tachycardia. I am very sorry!")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
