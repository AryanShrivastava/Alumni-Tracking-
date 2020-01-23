from django.db import models

# Create your models here.

class event_notify(models.Model):
    event_name = models.CharField(max_length=50,default="")
    date = models.DateField()
    time = models.TimeField(auto_now=True)
    venue = models.CharField(max_length=50, default="")
    about = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.event_name