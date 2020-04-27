

from django import forms
from .models import *
from ..login_reg.models import User

class RegisterCatForm(forms.Form):
    name = forms.CharField(max_length=255)
    desc = forms.CharField(max_length=1000, widget=forms.Textarea)



class RegisterDogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'











