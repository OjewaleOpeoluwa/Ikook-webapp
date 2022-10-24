from rest_framework import serializers
from .models import (Cuisine,SetMenu,addons,mainMenu,sideMenu,dessertMenu,starterMenu,MenuReviews)

class CuisineSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['name']

class SetMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = SetMenu
        fields = ['title','author','cusine','desc','price','status']

class AddonsSerializers(serializers.ModelSerializer):
    class Meta:
        model = addons
        fields = ['menu','author','title']

class MainMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = mainMenu
        fields = ['menu','author','title','s_price','p_price']

class SideMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = sideMenu
        fields = ['menu','author','title','s_price','p_price']

class DessertMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = dessertMenu
        fields = ['menu','author','title','s_price','p_price']

class StarterMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = starterMenu
        fields = ['menu','author','title','s_price','p_price']

class MenuReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuReviews
        fields = ['menu','author','rate','review']