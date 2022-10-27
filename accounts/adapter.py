from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.core.mail import send_mail as send_email

class MyAccountAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        # email = 'accounts/email/email_confirmation_message.txt'
        send_email('Subject',context,settings.DEFAULT_FROM_EMAIL,[email],fail_silently=False)
    
    # def get_email_confirmation_redirect_url(self, request):
    #     path = "http://localhost:3000/rest-auth/registration/verify-email/"
    #     return path.format(username=request.user.username)