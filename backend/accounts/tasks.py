from django.core.mail import EmailMessage
from celery.decorators import task

@task(name='send_email')
def send_emali(data):
    email = EmailMessage(subject=data['header'], body=data['text'],
                         to=[data['who']])
    email.send()
