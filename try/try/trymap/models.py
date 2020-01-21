from django.db import models

class loc(models.Model):
    lat = models.DecimalField(decimal_places=20, max_digits=30, blank=True, null=True, )
    longi = models.DecimalField(decimal_places=20, max_digits=30, blank=True, null=True, )
# Create your models here.
