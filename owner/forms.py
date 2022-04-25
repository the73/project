from django.forms import ModelForm
from owner.models import Admin
from django import forms

class OwnerForm(ModelForm):
    class Meta:
        model = Admin
        fields ="__all__"
        widgets = {
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "centers": forms.TextInput(attrs={"class": "form-control"}),
            "slots": forms.NumberInput(attrs={"class": "form-control"}),
        }