from django.urls import path
from .views import index, HomeView, ProfileView
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
]