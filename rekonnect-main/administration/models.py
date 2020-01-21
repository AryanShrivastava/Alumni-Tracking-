from django.db import models

# Create your models here.
class AdminModel(models.Model):
    username = models.CharField(unique=True, editable=True, max_length=50, primary_key=True)
    email = models.EmailField(editable=True)
    password = models.CharField(max_length=50)
    college_name = models.CharField(max_length=100)

    def __str__(self):
        return self.college_name


class Admin_userinfo(models.Model):
    username = models.ForeignKey(AdminModel, on_delete=models.CASCADE)
    stud_username = models.CharField(unique=True, editable=True, max_length=50)
    email = models.EmailField(editable=True)
    college_name = models.CharField(max_length=100)
