# myapp/views.py
import itertools

from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Game, Team, Player
from .serializers import UserStatisticsSerializer
from .permissions import CanViewTeamPlayers, CanViewPlayer, IsLeagueAdmin


class CustomLoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # This will automatically trigger the user_logged_in signal

            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'username': user.username,
                    'email': user.email,
                    'usertype': user.user_type
                }
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)


class GamesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rounds = [{'round': round,
                  'games': [{'date': game.date,
                  'round': game.round,
                  'home_team_id': game.home_team.id,
                  'away_team_id': game.away_team.id,
                  'home_team': game.home_team.name,
                  'away_team': game.away_team.name,
                  'home_team_score': game.home_team_score,
                  'away_team_score': game.away_team_score} for game in round_games]
                  } for round, round_games in itertools.groupby(Game.objects.all(), key=lambda g: g.round)]
        return JsonResponse({'rounds': rounds})

class TeamPlayersView(APIView):
    permission_classes = [CanViewTeamPlayers]

    def post(self, request):
        try:
            # need to check that the user is coach of the team or admin
            team_id = request.data.get('team')
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
        player_id = request.data.get('player')
        player = Player.objects.get(user__id=player_id)
        return JsonResponse({'name': player.user.get_full_name(),
                             'height': player.height,
                             'age': player.age,
                             'avg_score': player.avg_score,
                             'games_no': player.games_no})


class TeamView(APIView):
    permission_classes = [IsLeagueAdmin]

    def post(self, request):
        team_id = request.data.get('team')
        team = Team.objects.get(id=team_id)
        return JsonResponse({
                    'avg_score': team.avg_score,
                    'players': [{'id': player.user.id,
                                 'name': player.user.get_full_name(),
                                 'height': player.height,
                                 'age': player.age,
                                 'avg_score': player.avg_score,
                                 'games_no': player.games_no} for player in team.players]})


class UserStatisticsView(APIView):
    permission_classes = [IsLeagueAdmin]

    def get(self, request, format=None):
        # Only allow access to league_admin users
        if not request.user.is_authenticated or request.user.user_type != 'league_admin':
            return Response(status=403)

        users = User.objects.all()
        for user in users:
            if user.is_online():
                user.current_session_duration = timezone.now() - user.last_login_time
            else:
                user.current_session_duration = None
        serializer = UserStatisticsSerializer(users, many=True)
        return Response(serializer.data)