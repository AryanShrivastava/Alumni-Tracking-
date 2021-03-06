from django.urls import path
from .views import index, HomeView, ProfileView, DonationView, UpdateUser, SaveUser, saved, EventList, GalleryView
from django.contrib.auth.decorators import login_required

app_name = 'core'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('donation/', DonationView.as_view(), name='donation'),
    path('profile-update/', UpdateUser, name='profile-edit'),
    path('profile-save/', SaveUser, name='profile-save'),
    path('map/', saved, name='map'),
    path('events/', EventList.as_view(), name='events'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
]