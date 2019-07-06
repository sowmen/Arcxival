from django.contrib import admin
from .models import User, MyUserManager, user_type
# Register your models here.

admin.site.register(User)
admin.site.register(user_type)