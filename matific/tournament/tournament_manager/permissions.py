# permissions.py
from rest_framework.permissions import BasePermission

from .models import Team, Player

class IsLeagueAdmin(BasePermission):
    """
    Custom permission to only allow league admins to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and is a league admin
        return request.user.is_authenticated and request.user.user_type == 'league_admin'


class CanViewTeamPlayers(IsLeagueAdmin):
    """
    Custom permission to only allow league admins to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authorized
        if super().has_permission(request, view):
            return True
        try:
            team = Team.objects.get(id=request.POST.get('team'))
        except Team.DoesNotExist as e:
            return False

        if not team.coach: return False
        return request.user.is_authenticated and request.user.user_type == 'coach' and team.coach.id == request.user.id


class CanViewPlayer(IsLeagueAdmin):
    """
    Custom permission to only allow league admins to access the view.
    """

    def has_permission(self, request, view):
        # Check if the user is authorized
        if super().has_permission(request, view):
            return True
        try:
            player = Player.objects.get(user__id=request.POST.get('player'))
        except Player.DoesNotExist as e:
            return False

        return request.user.is_authenticated and request.user.user_type == 'coach' and player.user.team.coach.id == request.user.id

