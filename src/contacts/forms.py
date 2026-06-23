from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactRequest
        fields = ["name", "company", "email", "phone", "subject", "message"]

    def clean_honeypot(self):
        value = self.cleaned_data.get("honeypot", "")
        if value:
            raise forms.ValidationError("Spam detected.")
        return value

    def clean_name(self):
        value = self.cleaned_data.get("name", "").strip()
        if not value:
            raise forms.ValidationError("Введіть ваше ім'я.")
        return value

    def clean_message(self):
        value = self.cleaned_data.get("message", "").strip()
        if not value:
            raise forms.ValidationError("Введіть текст повідомлення.")
        return value
