from django import forms
from .models import Contact
from django.core.validators import validate_email

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"

        def validate(self, value):
            super().validate(value)
            for email in value:
                validate_email(email)