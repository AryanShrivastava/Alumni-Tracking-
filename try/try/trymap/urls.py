from . import views
from django.urls import path

urlpatterns = [
    path('', views.location, name='location'),
    path('savelocation/', views.savelocation, name='savelocation'),
    path('saved/', views.saved, name='saved'),
]