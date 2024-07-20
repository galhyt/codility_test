from django.urls import path
from .views import GamesView, TeamPlayersView, PlayerView, CustomLoginView, TeamView, UserStatisticsView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/login/', CustomLoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/games/', GamesView.as_view(), name='games'),
    path('api/team_players/', TeamPlayersView.as_view(), name='team_players'),
    path('api/player/', PlayerView.as_view(), name='player'),
    path('api/team/', TeamView.as_view(), name='team'),
    path('api/user_statistics/', UserStatisticsView.as_view(), name='user_statistics'),
]
