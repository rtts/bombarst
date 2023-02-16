from urllib.parse import quote
from django import forms
from django.conf import settings


class ContactForm(forms.Form):
    """
    Spam-resistant contact form.
    """

    body = forms.CharField(label="Uw bericht", widget=forms.Textarea(), required=False)

    def save(self):
        """
        Return a mailto: link.
        """

        subject = quote(settings.CONTACT_FORM_EMAIL_SUBJECT, safe="")
        body = quote(self.cleaned_data.get("body"), safe="")
        return f"mailto:{settings.CONTACT_FORM_EMAIL_ADDRESS}?subject={subject}&body={body}"
