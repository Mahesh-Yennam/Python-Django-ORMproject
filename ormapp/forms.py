from django import forms
from .models import Account, Education, Education2, Emp, Project

class EmpForm(forms.ModelForm):
    class Meta:
        model=Emp
        fields='__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model=Account
        fields='__all__'

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        fields="__all__"

class EducationForm2(forms.ModelForm):
    class Meta:
        model=Education2
        fields="__all__"

class ProjectFrom(forms.ModelForm):
    class Meta:
        model=Project
        fields="__all__"