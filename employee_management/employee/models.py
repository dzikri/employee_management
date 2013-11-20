# *--* coding utf-8*--*
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import ugettext_lazy as _


class Position(models.Model):
    """
    部署
    """
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u'部署:%s' % self.name


class UserProfile(models.Model):
    """
    user : Default User
    bio : ユーザの自己紹介
    """
    user = models.OneToOneField(User, unique=True)
    bio = models.TextField(_("bio"), null=True)
    position = models.ForeignKey(Position)

    def __unicode__(self):
        return u"%s さんのプロフィール" % self.user


class Post(models.Model):
    """
    とりあえず投稿
    """
    user = models.OneToOneField(User, unique=True)
    post = models.TextField(_("投稿"))
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s さんの投稿です。" % self.user


class Invite(models.Model):
    """
    飲みに行くテーブル
    sender さそった人
    to 誘われた人
    """
    author = models.OneToOneField(User)
    title = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%sさんが投稿したイベントの%sです" % self.author, self.title


class Attend(models.Model):
    invite = models.OneToOneField(Invite)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return u"%sさんがイベント%sに参加します。" % self.user, self.invite.title


def create_profile(sender, instance, created, **kwargs):
    """
    新規ユーザの作成
    """
    if created:
        # なかったら作り、あったら返す
        profile, created = UserProfile.objects.get_or_create(user=instance)


from django.db.models.signals import post_save
post_save.connect(create_profile, sender=User)
