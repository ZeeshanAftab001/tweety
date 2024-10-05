from django.contrib import admin
from . models import Profile
from django.contrib.auth.models import Group,User
from django.db.models.signals import post_save


admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model=Profile

class UserAdmin(admin.ModelAdmin):

    model=User
    fields=['username']
    inlines=[ProfileInline]

# admin.site.register(Profile)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)

# Register your models here.

def create_profile(sender,instance,created,**kwargs):

    if created:

        user_profile=Profile(user=instance)
        user_profile.save()

        user_profile.follows.set([instance.profile.id])


post_save.connect(create_profile,sender=User)




