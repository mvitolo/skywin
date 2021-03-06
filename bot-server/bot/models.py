from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from .validators import is_true


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=500, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    is_email_verified = models.BooleanField(default=False, )
    has_accepted_terms_and_conditions = models.BooleanField(validators=[is_true], default=False, )

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    @property
    def username(self):
        return self.user.username

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    def __unicode__(self):
        return u'%s' % self.user.username


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    tally = models.IntegerField(default=0)
    team = models.ForeignKey(Team, related_name='players')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.second_name)


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name="home_team")
    guest_team = models.ForeignKey(Team, related_name="guest_team")
    home_score = models.IntegerField(default=0)
    guest_score = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'

    def __unicode__(self):
        return u'%s %s - %s %s' % (self.home_team.name, self.home_score, self.guest_score, self.guest_team.name)
