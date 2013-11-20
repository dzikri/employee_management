from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import UserProfile, Post, Position, Invite, Attend


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )


admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)


class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)


class PositionAdmin(admin.ModelAdmin):

    class Meta:
        model = Position,

admin.site.register(Position, PositionAdmin)


class InviteAdmin(admin.ModelAdmin):
    class Meta:
        model = Invite

admin.site.register(Invite, InviteAdmin)


class AttendAdmin(admin.ModelAdmin):
    class Meta:
        model = Attend

admin.site.register(Attend, AttendAdmin)

