from rest_framework import serializers
from .models import Team, Player, Match


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = (
            'id',
            'first_name',
            'second_name',
            'tally',
            'team',
        )


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(many=True)

    class Meta:
        model = Team
        fields = (
            'id',
            'name',
            'players',
        )


class MatchSerializer(serializers.HyperlinkedModelSerializer):
    home_team = TeamSerializer()
    guest_team = TeamSerializer()

    class Meta:
        model = Match
        depth = 2
        fields = (
            'id',
            'home_team',
            'guest_team',
            'home_score',
            'guest_score',
        )
