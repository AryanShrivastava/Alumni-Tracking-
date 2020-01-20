from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms

# Create your views here.
class Signup(CreateView):
    form_class = forms.UserSignupForm
    success_url = reverse_lazy('registration:login')
    template_name = 'signup.html'