from django.contrib import admin
from .models import AdminModel, Admin_userinfo

# Register your models here.
admin.site.register(AdminModel)
admin.site.register(Admin_userinfo)
