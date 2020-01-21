from . import views
from django.urls import path

app_name = 'event'

urlpatterns = [
    path('', views.event, name="add_event"),
]