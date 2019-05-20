from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from .models import Profile
# Register your models here.

from .models import Post,Comment,Event

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Event)

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

       
     
        
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)