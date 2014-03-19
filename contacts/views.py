from django.views.generic.edit import FormView
from django.contrib import messages
from django.utils.translation import ugettext as _
from .forms import ContactsForm


class ContactsView(FormView):
    template_name = 'contacts/contacts.html'
    form_class = ContactsForm
    success_url = '/'

    def form_valid(self, form):
        try:
            form.send_mail()
        except Exception:
            messages.error(self.request, "Unknown error. Please try later.")
        else:
            messages.success(self.request,
                _("Your message has been successfully sent."))

        return super(ContactsView, self).form_valid(form)
