from django.contrib import admin
from .models import  Department, UserAdditionInfo, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserInline(admin.StackedInline):
    model = UserAdditionInfo
    can_delete = False


class NewUser(UserAdmin):
    inlines = [UserInline]

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image',)

admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, NewUser)    
admin.site.register(Department)


