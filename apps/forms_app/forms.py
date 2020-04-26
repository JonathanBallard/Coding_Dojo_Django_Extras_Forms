

from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=255)
    desc = forms.CharField(max_length=1000)
    desc2 = forms.CharField(max_length=1000)
    desc3 = forms.CharField(max_length=1000)
    desc4 = forms.CharField(max_length=1000)
    desc5 = forms.CharField(max_length=1000)
    desc6 = forms.CharField(max_length=1000)















