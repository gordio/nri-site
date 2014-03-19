from django.db import models
from django.utils.translation import ugettext_lazy as _


class Message(models.Model):
    email = models.EmailField(_("You email"), max_length=255)
    content = models.TextField(_("You message"), max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{0}: {1}'.format(self.pub_date, self.email)

    def __unicode__(self):
        return '{0}: {1}'.format(self.pub_date, self.email)