import os
from postmark import PMMail
import sendgrid

from sendgrid.helpers.mail import Email, Content, Mail


def sendEmailPostMark(subject, sender, to, body):
    message = PMMail(api_key = os.environ.get('POSTMARK_API_KEY'),
         subject = subject,
         sender = sender,
         to = to,
         text_body = body,
         tag = "contacto-web")

    enviado = message.send()
    return enviado


def sendEmailSendGrid(subject, sender, to, body):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(sender)
    to_email = Email(to)
    content = Content("text/plain", body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return response.status_code == 202
    #print(response.status_code)
    #print(response.body)
    #print(response.headers)