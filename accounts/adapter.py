from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.core.mail import send_mail as send_email

class MyAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        send_email('Subject',context,settings.DEFAULT_FROM_EMAIL,[email],fail_silently=False)
        