from django.shortcuts import render

# Create your views here.


def event(request):
    return render(request, 'event.html')
