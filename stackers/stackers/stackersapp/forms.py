from django import forms
from .models import Develop
from .models import Brief
from .models import QnA

# Develop ���� ������� form ����
class DevelopModelForm(forms.ModelForm):
    class Meta:
        model = Develop
        # fields = '__all__'
        fields = ['title', 'body']

        