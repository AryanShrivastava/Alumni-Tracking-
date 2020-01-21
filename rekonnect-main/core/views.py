from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from registration.models import Profile
import json
from event.models import event_notify

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

        profile = Profile.objects.get(user=request.user)
        profile.first_name = fname
        profile.last_name = lname
        profile.passout_year = passout_year
        profile.registration_number = reg
        profile.phone = phone
        
        profile.lat = lat
        profile.lng = lng
        
        profile.skills1 = skills1
        profile.skills2 = skills2
        profile.skills3 = skills3

        profile.proffesion = profession

        profile.save()
    return HttpResponseRedirect(reverse('core:profile'))

def saved(request):
    allentries = Profile.objects.values_list('lat', 'lng')
    locations = []
    for i in allentries:
        e = {'lat': float(i[0]), 'lng': float(i[1])}
        locations.append(e)
    print(locations)
    json_loc = json.dumps(locations)
    return render(request, 'map.html', {'data':json_loc})

class EventList(ListView):
    model = event_notify
    template_name = 'events.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'
