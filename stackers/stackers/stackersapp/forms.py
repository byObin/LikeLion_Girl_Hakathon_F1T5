from django import forms
from .models import Develop

# Develop 모델을 기반으로 form 생성
class DevelopModelForm(forms.ModelForm):
    class Meta:
        model = Develop
        # fields = '__all__'
        fields = ['title', 'body']