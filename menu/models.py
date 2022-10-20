from django.db import models

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User


class Cuisine (models.Model):
    name = models.CharField(max_length=75)

class SetMenu(models.Model):
    title = models.CharField(max_length=155)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    cusine = models.ForeignKey(Cuisine, on_delete=models.CASCADE)
    desc = models.CharField(max_length=255, null=True)
    price = models.FloatField(verbose_name='Starting Price')
    status = models.CharField

class addons(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='menu_addons',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)

class mainMenu(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='main_menu',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

class sideMenu(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='side_menu',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

class dessertMenu(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='dessert_menu',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)
    
class starterMenu(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='starter_menu',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

class MenuReviews(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='menu_reviews',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True)
    review = models.TextField(null=True)
    
# class menuGallery(models.Model):
#     banner_photo = models.ImageField(upload_to='uploads/menu/gallery/%Y/%m/%d/', blank=True, null=True)