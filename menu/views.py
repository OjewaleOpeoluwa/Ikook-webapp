from django.shortcuts import render
from rest_framework import generics

from .serializers import (CuisineSerializers,SetMenuSerializers,AddonsSerializers,MainMenuSerializers,
                            SideMenuSerializers,DessertMenuSerializers,StarterMenuSerializers,
                            MenuReviewsSerializers,MenuGallerySerializers,CheckOutSerializer)
from .models import (Cuisine,SetMenu,addons,mainMenu,sideMenu,dessertMenu,starterMenu,MenuReviews,MenuGallery,
                    CheckOut)

from .permissions import IsProfileChef


class CuisineViewSet(generics.ListCreateAPIView):
    serializer_class = CuisineSerializers
    queryset = Cuisine.objects.all()

class SetMenuViewSet(generics.ListCreateAPIView):
    permission_classes = [IsProfileChef]
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

class MenuGalleryViewSet(generics.ListCreateAPIView):
    serializer_class = MenuGallerySerializers
    queryset = MenuGallery.objects.all()

class CheckOutViewSet(generics.ListCreateAPIView):
    serializer_class = CheckOutSerializer
    queryset = CheckOut.objects.all()
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)