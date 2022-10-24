from django.shortcuts import render
from rest_framework import generics

from .serializers import (CuisineSerializers,SetMenuSerializers,AddonsSerializers,MainMenuSerializers,
                            SideMenuSerializers,DessertMenuSerializers,StarterMenuSerializers,
                            MenuReviewsSerializers)
from .models import (Cuisine,SetMenu,addons,mainMenu,sideMenu,dessertMenu,starterMenu,MenuReviews)

class CuisineViewSet(generics.ListCreateAPIView):
    serializer_class = CuisineSerializers
    queryset = Cuisine.objects.all()

class SetMenuViewSet(generics.ListCreateAPIView):
    serializer_class = SetMenuSerializers
    queryset = SetMenu.objects.all()

class AddonsViewSet(generics.ListCreateAPIView):
    serializer_class = AddonsSerializers
    queryset = SetMenu.objects.all()

class MainMenuViewSet(generics.ListCreateAPIView):
    serializer_class = MainMenuSerializers
    queryset = mainMenu.objects.all()

class SideMenuViewSet(generics.ListCreateAPIView):
    serializer_class = SideMenuSerializers
    queryset = sideMenu.objects.all()

class DessertMenuViewSet(generics.ListCreateAPIView):
    serializer_class = DessertMenuSerializers
    queryset = dessertMenu.objects.all()

class StarterMenuViewSet(generics.ListCreateAPIView):
    serializer_class = StarterMenuSerializers
    queryset = starterMenu.objects.all()

class MenuReviewsViewSet(generics.ListCreateAPIView):
    serializer_class = MenuReviewsSerializers
    queryset = MenuReviews.objects.all()
    