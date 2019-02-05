from django import forms
from models import User, Address, Media
from django.core.exceptions import ValidationError


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["last_name", "first_name", "gender", "email", "phone", "active"]
        exclude = ["fecha_alta", "fecha_modificacion"]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email.endswith('gmail.com'):
            raise ValidationError("Invalid email address.")

        return email


class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["country", "state", "city", "address", "zip_code"]


class MediaModelForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['name', 'url']
