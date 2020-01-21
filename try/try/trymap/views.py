from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from .models import loc
from django.http import HttpResponseRedirect
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return json.JSONEncoder.default(self, obj)

def location(request):
    return render(request, 'index.html')

def saved(request):
    allentries = loc.objects.values_list('lat', 'longi')
    locations = []
    for i in allentries:
        e = {'lat': float(i[0]), 'lng': float(i[1])}
        locations.append(e)
    print(locations)
    json_loc = json.dumps(locations)
    return render(request, 'nothing.html', {'data':json_loc})

def savelocation(request):
    if request.method == 'POST':
        lat = request.POST.get('lat')
        lon = request.POST.get('long')
        point = loc.objects.create(lat=lat, longi=lon)
        point.save()
        return HttpResponseRedirect(reverse('saved'))
    return HttpResponseRedirect(reverse('location'))
