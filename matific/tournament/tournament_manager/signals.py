import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from django.utils import timezone

from tournament_manager.models import User

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def user_logged_in_handler(sender, request, user, **kwargs):
    logger.debug(f"Signal received: User {user.username} is logging in.")
    user.login_count += 1
    user.last_login_time = timezone.now()
    user.save()
    logger.debug(f"User {user.username} login count updated to {user.login_count}.")

@receiver(user_logged_out)
def user_logged_out_handler(sender, request, **kwargs):
    user = User.objects.get(id=request.user.id)
    logger.debug(f"Signal received: User {user.username} is logging out.")
    user.last_logout_time = timezone.now()
    if user.last_login_time:
        user.total_time += timezone.now() - user.last_login_time
    user.save()
    logger.debug(f"User {user.username} total time spent updated to {user.total_time}.")
