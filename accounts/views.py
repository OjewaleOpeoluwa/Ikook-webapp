from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

from rest_auth.registration.views import SocialLoginView,SocialConnectView
from rest_auth.registration.serializers import SocialLoginSerializer 
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from rest_framework import generics

from .models import ChefProfile

from .serializers import ChefProfileSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter

# class RegisterView(CreateAPIView):
#     serializer_class = RegisterSerializer
#     permission_classes = register_permission_classes()
#     token_model = TokenModel
#     throttle_scope = 'dj_rest_auth'

#     @sensitive_post_parameters_m
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

#     def get_response_data(self, user):
#         if allauth_settings.EMAIL_VERIFICATION == \
#                 allauth_settings.EmailVerificationMethod.MANDATORY:
#             return {'detail': _('Verification e-mail sent.')}

#         if getattr(settings, 'REST_USE_JWT', False):
#             data = {
#                 'user': user,
#                 'access_token': self.access_token,
#                 'refresh_token': self.refresh_token,
#             }
#             return JWTSerializer(data, context=self.get_serializer_context()).data
#         elif getattr(settings, 'REST_SESSION_LOGIN', False):
#             return None
#         else:
#             return TokenSerializer(user.auth_token, context=self.get_serializer_context()).data

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         data = self.get_response_data(user)

#         if data:
#             response = Response(
#                 data,
#                 status=status.HTTP_201_CREATED,
#                 headers=headers,
#             )
#         else:
#             response = Response(status=status.HTTP_204_NO_CONTENT, headers=headers)

#         return response

#     def perform_create(self, serializer):
#         user = serializer.save(self.request)
#         if allauth_settings.EMAIL_VERIFICATION != \
#                 allauth_settings.EmailVerificationMethod.MANDATORY:
#             if getattr(settings, 'REST_USE_JWT', False):
#                 self.access_token, self.refresh_token = jwt_encode(user)
#             elif not getattr(settings, 'REST_SESSION_LOGIN', False):
#                 # Session authentication isn't active either, so this has to be
#                 #  token authentication
#                 create_token(self.token_model, user, serializer)

#         complete_signup(
#             self.request._request, user,
#             allauth_settings.EMAIL_VERIFICATION,
#             None,
#         )
#         return user


class ChefProfileList(generics.ListCreateAPIView):
    serializer_class = ChefProfileSerializer
    queryset = ChefProfile.objects.all()

class ChefProfileDetail(generics.RetrieveAPIView):
    serializer_class = ChefProfileSerializer
    queryset = ChefProfile.objects.all()