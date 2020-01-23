from django.urls import path, include
from .views import login, index, logout, event, push_event

app_name = 'administration'

urlpatterns = [
    path('login/', login, name='login'),
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('event/', event, name='event'),
    path('push/', push_event, name='push_event')
]