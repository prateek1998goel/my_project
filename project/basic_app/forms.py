from django import forms
from basic_app.models import School

class form(forms.ModelForm):
    class Meta():
        model=School
        fields="__all__"
