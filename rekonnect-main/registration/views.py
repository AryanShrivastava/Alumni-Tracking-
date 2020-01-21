from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .models import Profile

from .forms import UserSignupForm

def SignUp(request):
    form = UserSignupForm()
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'])
            login(request, new_user)
            p = User.objects.get(id=request.user.id)
            Profile.objects.create(user=p)
            return HttpResponseRedirect(reverse_lazy('core:home'))
    return render(request, 'signup.html', {'form':form})