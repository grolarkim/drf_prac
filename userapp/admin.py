from django.contrib import admin
from userapp.models import User, UserProfile, Hobby, UserProfileHobby

# Register your models here.

class HobbyInline(admin.TabularInline):
    model = UserProfileHobby

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", )
    inlines = (HobbyInline,)

admin.site.register(User)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Hobby)
# admin.site.register(UserProfileHobby)