from django.views.generic import CreateView
from django.urls import reverse_lazy

from . import forms

class SignUp(CreateView):
    # form_class = forms.UserSignupForm
    # success_url = reverse_lazy('registration:login')
    # template_name = ''
    pass