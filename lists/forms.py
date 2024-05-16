from django import forms
from .models import ListTemplate

class ListCreateForm(forms.ModelForm):
    class Meta:
        model = ListTemplate
        fields = ['list_title']

