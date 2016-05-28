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


class Player(models.Model):
    firstName = models.CharField(max_length=100)
    secondName = models.CharField(max_length=100)
    tally = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name
