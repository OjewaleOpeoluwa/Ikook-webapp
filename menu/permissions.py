from rest_framework import permissions
from accounts.models import MyUser

class IsProfileChef(permissions.BasePermission):

    def has_permission(self,request,view):
        user = request.user
        test = MyUser.objects.filter(profile__chef_profile = user.id).exists()
        return test

