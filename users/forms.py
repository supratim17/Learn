from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    #first_name = forms.CharField(max_length=100)
    # rest of the fields

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # you can validate those here

    class Meta:
        model = User