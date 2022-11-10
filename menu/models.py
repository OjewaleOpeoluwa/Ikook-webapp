from django.db import models

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager,User
from django.conf import settings
from datetime import datetime



class Cuisine (models.Model):
    name = models.CharField(max_length=75)

    def __str__(self) -> str:
        return self.name



class addons(models.Model):
    # menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='menu_addons',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

    def __str__(self) -> str:
        return self.title

class mainMenu(models.Model):
    # menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='main_menu',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)


    def __str__(self) -> str:
        return self.title

class sideMenu(models.Model):
    # menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='side_menu',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

    def __str__(self) -> str:
        return self.title

class dessertMenu(models.Model):
    # menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='dessert_menu',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

    def __str__(self) -> str:
        return self.title

class starterMenu(models.Model):
    # menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='starter_menu',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    s_price = models.CharField(max_length=125, verbose_name='Sharing price', null=True)
    p_price = models.CharField(max_length=125, verbose_name='platted price', null=True)

    def __str__(self) -> str:
        return self.title



class MenuGallery(models.Model):
    banner_photo = models.URLField(max_length=255, blank=True, null=True)


class SetMenu(models.Model):
    title = models.CharField(max_length=155)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cusine = models.ManyToManyField(Cuisine,related_name="cusines",blank=True)
    addons = models.ManyToManyField(addons,related_name="addons",blank=True)
    main_menu = models.ManyToManyField(mainMenu,related_name="main_menu",blank=True)
    side_menu = models.ManyToManyField(sideMenu,related_name="side_menu",blank=True)
    dessert_menu = models.ManyToManyField(dessertMenu,related_name="dessert_menu",blank=True)
    starter_menu = models.ManyToManyField(starterMenu,related_name="starter_menu",blank=True)
    desc = models.CharField(max_length=255, null=True)
    price = models.FloatField(verbose_name='Starting Price')
    status = models.CharField(max_length=255,blank=True)
    menu_gallery = models.ManyToManyField(MenuGallery,related_name="gallery")

    def __str__(self) -> str:
        return self.title

class MenuReviews(models.Model):
    menu = models.ForeignKey(SetMenu, on_delete=models.SET_NULL, related_name='menu_reviews',null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rate = models.IntegerField(null=True)
    review = models.TextField(null=True)

    def __str__(self) -> str:
        return str(self.author)


class CheckOut(models.Model):
    DELIVERY = [
        ('PHY','Physical'),
        ('GOU','Gourmet'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    event_name = models.CharField(max_length=255)
    address_name = models.CharField(max_length=200)
    delivery = models.CharField(max_length=30,choices=DELIVERY)
    time = models.DateTimeField(default=datetime.now())
    description = models.TextField()