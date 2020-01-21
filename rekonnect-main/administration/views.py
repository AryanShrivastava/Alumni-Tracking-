from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from .models import AdminModel

logged_in = False

# Create your views here.
def login(request):
    global logged_in
    if logged_in:
        return HttpResponseRedirect(reverse('administration:index'))
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        s = AdminModel.objects.filter(username = username, email = email)
        if s.count() == 1:
            logged_in = True
            return HttpResponseRedirect(reverse('administration:index'))
    return render(request, 'admin-login.html', {})

def redirect_login(request):
    global logged_in
    if logged_in == False:
        return HttpResponseRedirect(reverse('administration:login'))

def index(request):
    redirect_login(request)
    return render(request, 'admin-index.html', {})

def logout(request):
    global logged_in
    if logged_in:
        logged_in = False
    return HttpResponseRedirect(reverse('core:index'))

def massmailer(request):
    send_mail('HELLO THIS IS SUBJECT',
              "HELLO THIS IS TesT",
              'devaryan.gfgsrm@gmail.com',
              ['ss1874@srmist.edu.in','absa0545@gmail.com', 'devaryan.gfgsrm@gmail.com'],
              fail_silently=False)
