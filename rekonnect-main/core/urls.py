from django.urls import path
from .views import index, HomeView

app_name = 'core'

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('home/', HomeView.as_view(), name='home'),
]