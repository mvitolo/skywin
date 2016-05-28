from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets
from .models import Team, Player, Match
from .serializers import TeamSerializer, PlayerSerializer, MatchSerializer


# ===========================================================================
# HOME
# ===========================================================================
def home(request, template_name="bot/home.html"):
    return render_to_response(template_name, {
        'session': request.session.keys(),
    }, context_instance=RequestContext(request))


#########################################
# Django REST framework                 #
# http://www.django-rest-framework.org/ #
#########################################
class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
