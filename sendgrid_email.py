import sendgrid
import os
from sendgrid.helpers.mail import *


sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('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'))
from_email = Email("livigwynn_5_@hotmail.co.uk")
to_email = Email("olivia.gwynn@duke.edu")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)