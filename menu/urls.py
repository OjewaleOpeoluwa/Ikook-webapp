from django.urls import path,re_path,include
from rest_framework import routers

from .views import (CuisineViewSet,SetMenuViewSet,AddonsViewSet,MainMenuViewSet,
                    SideMenuViewSet,DessertMenuViewSet,StarterMenuViewSet,
                    MenuReviewsViewSet)

urlpatterns = [
    path('cuisine', CuisineViewSet.as_view(),name='cuisine'),
    path('setmenu', SetMenuViewSet.as_view(),name='set_menu'),
    path('addons', AddonsViewSet.as_view(),name='addons'),
    path('mainmenu', MainMenuViewSet.as_view(),name='main_menu'),
    path('sidemenu', SideMenuViewSet.as_view(),name='side_menu'),
    path('dessert', DessertMenuViewSet.as_view(),name='dessert'),
    path('starter', StarterMenuViewSet.as_view(),name='starter'),
    path('menureviews', MenuReviewsViewSet.as_view(),name='menu_reviews'),

]