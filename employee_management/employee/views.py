# coding utf8
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
# from django.core.urlresolvers import reverse
from .models import UserProfile
# from .form import UserProfileForm


class UserProfileView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "users/user_profile.html"

    def get_object(self, queryset=None):
        """
        ユーザIdをプロフィールから探し、あれば返す。なければ作る
        """
        user = super(UserProfileView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user
