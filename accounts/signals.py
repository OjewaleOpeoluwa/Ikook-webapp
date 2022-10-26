from  .models import Profile,ChefProfile
from django.db.models.signals import post_save,post_delete
from django.conf import settings

def createProfile(sender,instance,created,**kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            name = user.username,
            # email = user.email,
            # username = user.first_name,
        )

def createTypeProfile(sender,instance,created,**kwargs):
    if created:
        profile = instance
        if profile.get_user_type_display() == 'chef':
            profile = ChefProfile.objects.create(
                profile = profile,
                is_chef = True,
                # email = user.email,
                # username = user.first_name,
            )

post_save.connect(createProfile,sender=settings.AUTH_USER_MODEL)
post_save.connect(createTypeProfile,sender=Profile)