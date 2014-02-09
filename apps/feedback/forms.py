from django import forms
from django.conf import settings
from django.core.mail import send_mail as django_send_mail
from django.utils.translation import ugettext_lazy as _
from .models import Message


class ContactsForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['email', 'content']

    def send_mail(self):
        return django_send_mail(
            _("{0} This message sended from you site.".format(settings.EMAIL_PREFIX)),
            self.cleaned_data['content'],
            self.cleaned_data['email'],
            [manager[1] for manager in settings.MANAGERS]
        )