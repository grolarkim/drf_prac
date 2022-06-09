from django.contrib import admin
from userapp.models import User, UserProfile, Hobby, UserProfileHobby

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobby)
admin.site.register(UserProfileHobby)