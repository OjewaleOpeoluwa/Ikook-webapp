from django.urls import path
from .views import ChefProfileList,ChefProfileDetail

urlpatterns = [
    path('cheflist/',ChefProfileList.as_view(),name='cheflist'),
    path('chefdetail/<int:pk>/',ChefProfileDetail.as_view(),name='chefdetail'),
]
