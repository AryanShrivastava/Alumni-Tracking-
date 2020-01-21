from django.urls import path
from .views import login, index, logout

app_name = 'administration'

urlpatterns = [
    path('login/', login, name='login'),
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
    path('event/', include('event.urls')),
]