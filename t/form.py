from django import forms
from .models import Disease


class DiseaseForm(forms.Form):
    name = forms.CharField(max_length=40)
