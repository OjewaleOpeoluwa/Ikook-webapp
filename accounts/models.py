from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True,default='00000000')

class Profile(models.Model):
    user = models.OneToOneField(MyUser, primary_key=True, verbose_name='Profile', related_name='profile', on_delete=models.CASCADE)
    type = [('chef', 'chef'),
                ('customer','customer'),
                ('customer','customer'),
                ('admin','admin'),
                ('author','author'),
                ]
    user_type = models.CharField(max_length=8, choices=type)
    name = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    # profile_photo = models.ImageField(upload_to='uploads/profile/%Y/%m/%d/', blank=True, null=True)
    followers = models.ManyToManyField(MyUser, blank=True, related_name='followers')
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

class ChefProfile(models.Model):
    profile = models.OneToOneField(Profile, primary_key=True, verbose_name='Chef Profile', related_name='chef_profile', on_delete=models.CASCADE)
    headline = models.CharField(max_length=500, blank=True, null=True)
    languages = models.CharField(max_length=500, blank=True, null=True)
    is_chef = models.BooleanField(default=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    # banner_photo = models.ImageField(upload_to='uploads/banner/%Y/%m/%d/', blank=True, null=True)
    
    def __str__(self):
        return self.profile.name

class MealPrep(models.Model):
    profile = models.OneToOneField(ChefProfile, verbose_name='User Service', related_name='user_service', on_delete=models.CASCADE)
    prep_type = [('weekly', 'weekly'),
                ('monthly','monthly'),]
    prep = models.CharField(max_length=7, choices=prep_type, verbose_name='Service Type', default=" ")
    service_type = models.CharField(max_length=19, ) #Physical or Gourmet or both
    price = models.IntegerField(verbose_name='Start Price')