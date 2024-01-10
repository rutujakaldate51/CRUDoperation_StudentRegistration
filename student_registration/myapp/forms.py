from django.core import validators
from django import forms
from .models import Student



class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','mobile', 'address','skill', 'gender']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'skill': forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.TextInput(attrs={'class':'form-control'}),
        }