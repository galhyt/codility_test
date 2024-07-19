from django.contrib.auth.models import AbstractUser
from django.db import models

# Custom user model
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('league_admin', 'League Admin'),
        ('coach', 'Coach'),
        ('player', 'Player'),
    )
    user_type = models.CharField(max_length=30, choices=USER_TYPE_CHOICES)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL, related_name='members')

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    height = models.FloatField()
    age = models.FloatField()

    def __str__(self):
        return f"{self.user.first_name} ({self.user.id})"

    def save(self, *args, **kwargs):
        if self.user.user_type != 'player':
            raise ValueError("The related user must be of type 'player'.")
        super().save(*args, **kwargs)

    @property
    def avg_score(self):
        stats = GameStats.objects.filter(player=self.user.id)
        scores = sum(map(lambda stat: stat.score, stats))
        return scores / len(stats)

    @property
    def games_no(self):
        stats = GameStats.objects.filter(player=self.user.id)
        return len(stats)

# Team model
class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.id})"

    @property
    def players(self):
        return list(Player.objects.filter(user__team=self.id, user__user_type='player'))

    @property
    def coach(self):
        coaches = User.objects.filter(team=self.id, user_type='coach')
        if not coaches: return None
        return coaches[0]

    @property
    def avg_score(self):
        home_games = self.home_games.all()
        away_games = self.away_games.all()
        score = sum(map(lambda game: game.home_team_score, home_games))
        score += sum(map(lambda game: game.away_team_score, away_games))
        games_no = len(home_games) + len(away_games)
        return score / games_no


# Game model
class Game(models.Model):
    date = models.DateTimeField()
    round = models.IntegerField(null=True)
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    home_team_score = models.IntegerField(default=0)
    away_team_score = models.IntegerField(default=0)

    def __str__(self):
        team_won = self.home_team if self.home_team_score > self.away_team_score else self.away_team
        return f"{self.home_team} vs {self.away_team} on {self.date} round {self.round} - {team_won} won"

class GameStats(models.Model):
    game = models.ForeignKey('Game', null=True, blank=True, on_delete=models.SET_NULL, related_name='stats')
    player = models.ForeignKey('Player', null=True, blank=True, on_delete=models.SET_NULL, related_name='stats')
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.game} {self.player} {self.score}"
