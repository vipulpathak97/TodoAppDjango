from django import forms
from .models import Task

class Taskform(forms.ModelForm):
    class meta:
        model = Task
        fields = ["item", "completed"]