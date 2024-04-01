from django import forms

from accounts.models import Shoppers


class SignUp(forms.ModelForm):
    city = forms.CharField(max_length=60)
    phone_number = forms.CharField(max_length=10)
    location = forms.CharField(max_length=255)

    class Meta:
        model = Shoppers
        fields = ["username", "first_name", "last_name", "email", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
    pass


class LoginForm(forms.ModelForm):

    class Meta:
        model = Shoppers
        fields = ["username", "password"]

        widgets = {
            "password": forms.PasswordInput(),
        }
        pass
    pass

