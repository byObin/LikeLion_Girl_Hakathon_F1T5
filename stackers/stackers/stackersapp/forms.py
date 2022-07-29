from ast import Break
from django import forms
from .models import Develop, Brief, QnA


class DevelopModelForm(forms.ModelForm):
    class Meta:
        model = Develop
        # fields = '__all__'
        fields = ['title', 'body']

class BriefModelForm(forms.ModelForm):
    class Meta:
        model = Brief
        fields = ['title', 'body', 'photo']

class QnAModelForm(forms.ModelForm):
    class Meta:
        model = QnA
        fields = ['title', 'body', 'photo']
