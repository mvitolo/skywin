from django.conf.urls import patterns, url
from rest_framework import routers
from .views import TeamViewSet, PlayerViewSet, MatchViewSet, IndexView, DetailView, ResultsView, vote


urlpatterns = patterns(
    'bot.views',

    # Home
    # (r'^[/]?$', 'home', {'template_name': 'bot/home.html'}, 'bot_home'),

    # Telegram Bot
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', vote, name='vote'),

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
