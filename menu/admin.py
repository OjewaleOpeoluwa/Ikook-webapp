from django.contrib import admin
from .models import (Cuisine,SetMenu,addons,mainMenu,sideMenu,dessertMenu,starterMenu,MenuReviews)

admin.site.register(Cuisine)
admin.site.register(SetMenu)
admin.site.register(addons)
admin.site.register(mainMenu)
admin.site.register(sideMenu)
admin.site.register(dessertMenu)
admin.site.register(starterMenu)
admin.site.register(MenuReviews)