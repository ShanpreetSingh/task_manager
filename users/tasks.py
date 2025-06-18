from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import get_user_model

@shared_task(bind=True)
def send_welcome_email(self, user_id):
    User = get_user_model()
    try:
        user = User.objects.get(id=user_id)
        subject = 'Welcome to Task Manager'
        message = (
            f'Hi {user.username},\n\n'
            'Thank you for registering with our Task Manager service!\n\n'
            'Best regards,\n'
            'Task Manager Team'
        )
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist as e:
        self.retry(exc=e, countdown=60, max_retries=3)