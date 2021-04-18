from django.core.mail import EmailMessage
#@task(name='send_edata')
def send_emali(data):
    email = EmailMessage(subject=data['header'], body=data['text'], to=[data['who']])
    email.send()
