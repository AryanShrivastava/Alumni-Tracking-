from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User

# Create your views here.
class index(TemplateView):
    template_name = 'intro.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.id)

class DonationView(TemplateView):
    template_name = 'donation.html'