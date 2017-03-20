import django
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models, connection
from django.db.models.fields.related import create_many_related_manager, ManyToManyRel
from django.utils.translation import ugettext_lazy as _

from .compat import User
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """
    1. 팔로우, 차단을 함께 만들 수 있는 중간자모델을 구현(검색, django follower twitter model)
    2. MyUser의 메서드로 follow, block, friends, following_list, follower_list
    """
    def to_dict(self):
        ret = {
            'pk': self.pk,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
        }
        return ret


class RelationshipStatusManager(models.Manager):
    def following(self):
        return self.get(from_slug='following')

    def blocking(self):
        return self.get(from_slug='blocking')

    def by_slug(self, status_slug):
        return self.get(
            models.Q(from_slug=status_slug) |
            models.Q(to_slug=status_slug) |
            models.Q(symmetrical_slug=status_slug)
        )


class RelationshipStatus(models.Model):
    name = models.CharField(_('name'), max_length=100)
    verb = models.CharField(_('verb'), max_length=100)
    from_slug = models.CharField(_('from slug'), max_length=100,
        help_text=_("Denote the relationship from the user, i.e. 'following'"))
    to_slug = models.CharField(_('to slug'), max_length=100,
        help_text=_("Denote the relationship to the user, i.e. 'followers'"))
    symmetrical_slug = models.CharField(_('symmetrical slug'), max_length=100,
        help_text=_("When a mutual relationship exists, i.e. 'friends'"))
    login_required = models.BooleanField(_('login required'), default=False,
        help_text=_("Users must be logged in to see these relationships"))
    private = models.BooleanField(_('private'), default=False,
        help_text=_("Only the user who owns these relationships can see them"))

    objects = RelationshipStatusManager()

    class Meta:
        ordering = ('name',)
        verbose_name = _('Relationship status')
        verbose_name_plural = _('Relationship statuses')

    def __unicode__(self):
        return self.name
