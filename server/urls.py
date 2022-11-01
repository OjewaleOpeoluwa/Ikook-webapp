"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from accounts.views import FacebookLogin,FacebookConnect,GoogleConnect,GoogleLogin
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Authentication API",
      default_version='v2',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^rest-auth/', include('rest_auth.urls')),
    re_path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
        # Password reset
    re_path(r'^rest-auth/password/reset/<uidb64>/<token>/',
         PasswordResetView.as_view(),
         name='rest_password_reset'
         ),

    re_path(r'^rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),
    re_path(r'^rest-auth/google/$', GoogleLogin.as_view(), name='go_login'),
    re_path(r'^rest-auth/google/connect/$', GoogleConnect.as_view(), name='go_connect'),
    re_path(
            r'^socialaccounts/$',
            SocialAccountListView.as_view(),
            name='social_account_list'
        ),
    re_path(
            r'^socialaccounts/(?P<pk>\d+)/disconnect/$',
            SocialAccountDisconnectView.as_view(),
            name='social_account_disconnect'
        ),
    re_path(r'^authenticate/', include('allauth.urls'), name='socialaccount_signup'),
     path('user/password/reset/',
         PasswordResetView.as_view(),
         name='rest_password_reset'
         ),

    path('user/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('menu/',include('menu.urls')),
    path('accounts/',include('accounts.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]


