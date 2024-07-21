import datetime
import itertools
import random
import time
from copy import copy, deepcopy

from django.core.management.base import BaseCommand, CommandError
from tournament_manager.models import Game, User, Player, Team, GameStats


class Command(BaseCommand):
    help = 'Describe what your custom command does here'

    # def add_arguments(self, parser):
    #     # Add command line arguments here if needed
    #     parser.add_argument('sample_arg', type=int, help='Sample argument description')

    def handle(self, *args, **options):
        GameStats.objects.all().delete()
        Game.objects.all().delete()
        Player.objects.all().delete()
        User.objects.exclude(id=1).delete()
        Team.objects.all().delete()

        self.create_teams()
        self.create_users()
        self.create_games()

        self.stdout.write(self.style.SUCCESS('Successfully executed command'))

    def create_teams(self):
        for n in range(1, 17):
            name = f"Team_{n}"
            Team.objects.create(name=name)

    def create_users(self):
        # create league_admin user
        name = f"league_admin"
        user = User.objects.create(username=name, first_name=name, last_name=name, email=f"{name}@gmail.com",
                                   user_type='league_admin')
        user.set_password('universite')
        user.save()

        for team in Team.objects.all():
            # create players
            for n in range(1, 11):
                name = f"{team.name}_player_{n}"
                user = User.objects.create(username=name, first_name=name, last_name=name, email=f"{name}@gmail.com", user_type='player', team=team)
                height = random.randint(180, 200) / 100
                age = random.randint(18, 40)
                Player.objects.create(user=user, height=height, age=age)

            # create coach
            name = f"{team.name}_coach"
            user = User.objects.create(username=name, first_name=name, last_name=name, email=f"{name}@gmail.com", user_type='coach', team=team)
            user.set_password('universite')
            user.save()

    def create_games(self):
        game_date = datetime.datetime.now()
        teams = list(Team.objects.all())
        for round in range(1, 5):
            self.create_round_games(game_date, round, teams)
            game_date += datetime.timedelta(days=7)

    def create_round_games(self, game_date, round, teams):
        n = len(teams)
        _teams = deepcopy(teams)
        while n > 0:
            idx1 = random.randint(0, n-1)
            team1 = _teams.pop(idx1)
            players_no = random.randint(5, 10)
            players1 = random.sample(team1.players, k=players_no)
            players_scores1 = [random.randint(0, 20) for _ in range(len(players1))]
            team1_score = sum(players_scores1)
            n -= 1
            idx2 = random.randint(0, n-1)
            team2 = _teams.pop(idx2)
            players_no = random.randint(5, 10)
            players2 = random.sample(team2.players, k=players_no)
            players_scores2 = [random.randint(0, 20) for _ in range(len(players2))]
            team2_score = sum(players_scores2)
            n -= 1
            if team1_score == team2_score:
                team2_score += 1
                players_scores2[0] += 1

            # create game
            game = Game.objects.create(date=game_date, round=round, home_team=team1, away_team=team2, home_team_score=team1_score, away_team_score=team2_score)
            self.create_game_stats(game, players1, players_scores1)
            self.create_game_stats(game, players2, players_scores2)
            # remove the lost team from teams
            lost_team = team1 if team2_score > team1_score else team2
            teams.remove(lost_team)

    def create_game_stats(self, game, players, players_scores):
        for i in range(len(players)):
            player_score = players_scores[i]
            player = players[i]
            GameStats.objects.create(game=game, player=player, score=player_score)


if __name__ == '__main__':
    Command().handle()
