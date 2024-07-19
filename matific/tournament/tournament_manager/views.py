# myapp/views.py
from django.http import JsonResponse
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Game, Team, Player
from .permissions import CanViewTeamPlayers, CanViewPlayer, IsLeagueAdmin


class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'username': user.username,
                    'email': user.email,
                }
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class GamesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        games = [{'date': game.date,
                  'round': game.round,
                  'home_team_id': game.home_team.id,
                  'away_team_id': game.away_team.id,
                  'home_team': str(game.home_team),
                  'away_team': str(game.away_team),
                  'home_team_score': game.home_team_score,
                  'away_team_score': game.away_team_score} for game in Game.objects.all()]
        return JsonResponse({'games': games})

class TeamPlayersView(APIView):
    permission_classes = [CanViewTeamPlayers]

    def post(self, request):
        try:
            # need to check that the user is coach of the team or admin
            team_id = request.POST.get('team')
            team = Team.objects.get(id=team_id)
        except Exception as e:
            print(e)
        return JsonResponse({'players': [{'id': player.user.id,
                                          'name': player.user.get_full_name(),
                                          'height': player.height,
                                          'age': player.age} for player in team.players]})


class PlayerView(APIView):
    permission_classes = [CanViewPlayer]

    def post(self, request):
        # need to check that the user is coach of the team or admin
        player_id = request.POST.get('player')
        player = Player.objects.get(user__id=player_id)
        return JsonResponse({'name': player.user.get_full_name(),
                             'height': player.height,
                             'age': player.age,
                             'avg_score': player.avg_score,
                             'games_no': player.games_no})


class TeamView(APIView):
    permission_classes = [IsLeagueAdmin]

    def post(self, request):
        team_id = request.POST.get('team')
        team = Team.objects.get(id=team_id)
        return JsonResponse({
                    'avg_score': team.avg_score,
                    'players': [{'name': player.user.get_full_name(),
                                 'height': player.height,
                                 'age': player.age,
                                 'avg_score': player.avg_score,
                                 'games_no': player.games_no} for player in team.players]})