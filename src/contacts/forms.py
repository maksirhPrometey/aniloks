from django import forms

from .choices import OTHER_VALUE, build_subject_choices
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = ContactRequest
        fields = ["name", "company", "email", "phone", "subject", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["subject"].widget = forms.Select(
            attrs={"class": "form__select"},
        )
        grouped_choices, allowed_values = build_subject_choices(compact=True)
        self.fields["subject"].choices = grouped_choices
        self._allowed_subject_values = allowed_values

        if not self.is_bound and not self.initial.get("subject"):
            first_value = self._first_subject_value(grouped_choices)
            if first_value:
                self.fields["subject"].initial = first_value

    @staticmethod
    def _first_subject_value(grouped_choices):
        for _group_name, options in grouped_choices:
            for value, _label in options:
                if value != OTHER_VALUE:
                    return value
        return OTHER_VALUE

    def clean_subject(self):
        value = self.cleaned_data.get("subject", "").strip()
        if value not in self._allowed_subject_values:
            raise forms.ValidationError("Оберіть категорію продукту зі списку.")
        return value

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
