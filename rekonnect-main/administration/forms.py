from django import forms
from .models import AdminModel

class AdminForm(forms.ModelForm):
    class Meta:
        model = AdminModel
        widgets = {
            'password': forms.PasswordInput(attrs={}),
        }