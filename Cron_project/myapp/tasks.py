from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_scheduled_email():
    subject = 'Hello from Django + Celery'
    message = 'This is a scheduled email sent by Celery.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['shivprasad129806@gmail.com']  # your second mail

    send_mail(subject, message, from_email, recipient_list)
    return "Email sent!"
