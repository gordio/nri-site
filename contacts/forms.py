from django import forms
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
from .models import Message


class ContactsForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Message
        fields = ['email', 'content']

    def send_mail(self):
        return django_send_mail(
            _("{0} New message from site".format(settings.EMAIL_PREFIX)),
            self.cleaned_data['content'],
            self.cleaned_data['email'],
            [manager[1] for manager in settings.MANAGERS]
        )
