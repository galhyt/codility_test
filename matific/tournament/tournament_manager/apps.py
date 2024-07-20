from django.apps import AppConfig


class TournamentManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tournament_manager'

    def ready(self):
        import tournament_manager.signals