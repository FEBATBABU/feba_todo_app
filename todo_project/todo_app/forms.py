from django.forms import fields

from . models import Task
from django import forms
class Todoforms(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']