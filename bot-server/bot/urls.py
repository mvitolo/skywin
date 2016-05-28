from django.conf.urls import patterns, include, url
from rest_framework import routers
from .views import TeamViewSet, PlayerViewSet, MatchViewSet


urlpatterns = patterns(
    'bot.views',

    # Home
    # (r'^[/]?$', 'home', {'template_name': 'bot/home.html'}, 'bot_home'),

)


#########################################
# Django REST framework                 #
# http://www.django-rest-framework.org/ #
#########################################

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)
