from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import PWtest

# Create your views here.
def signup(request):
    if request.method == 'POST':
        pw = request.POST.get('pw')
        