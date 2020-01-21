from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passout_year = models.IntegerField(default=1990)
    registration_number = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)

    lat = models.DecimalField(decimal_places=20, max_digits=20, blank=True, null=True)
    lng = models.DecimalField(decimal_places=20, max_digits=20, blank=True, null=True)

    skills1 = models.CharField(max_length=100)
    skills2 = models.CharField(max_length=100)
    skills3 = models.CharField(max_length=100)

    proffesion = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

