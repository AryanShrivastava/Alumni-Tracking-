from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from registration.models import User 

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

def UpdateUser(request):
    return render(request, 'profile-edit.html')

def SaveUser(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name', '')
        lname = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        passout_year = request.POST.get('year', '')
        reg = request.POST.get('reg', '')
        phone = request.POST.get('phone', '')
        
        profession = request.POST.get('proffesion', '')

        skills1 = request.POST.get('skill1', '')
        skills2 = request.POST.get('skill2', '')
        skills3 = request.POST.get('skill3', '')

        lat = request.POST.get('lat')
        lng = request.POST.get('lng')

        user = User.objects.get(id=request.user.id)
        user.first_name = fname
        user.last_name = lname
        user.passout_year = passout_year
        user.registration_number = reg
        user.phone = phone
        
        user.lat = lat
        user.lng = lng
        
        user.skills1 = skills1
        user.skills2 = skills2
        user.skills3 = skills3

        user.proffesion = profession

        user.save()
    return HttpResponseRedirect(reverse('core:profile'))