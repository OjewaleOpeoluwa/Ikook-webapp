from django.contrib import admin
from .models import MyUser,Profile,ChefProfile

admin.site.register(MyUser)
admin.site.register(Profile)
admin.site.register(ChefProfile)