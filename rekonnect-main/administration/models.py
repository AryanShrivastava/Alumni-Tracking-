from django.db import models

# Create your models here.
class AdminModel(models.Model):
    username = models.CharField(unique=True, editable=False, max_length=50)
    email = models.EmailField(editable=False)
    password = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name