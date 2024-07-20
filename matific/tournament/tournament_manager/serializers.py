from django.utils import timezone
from rest_framework import serializers
from .models import User

class UserStatisticsSerializer(serializers.ModelSerializer):
    is_online = serializers.SerializerMethodField()
    current_session_duration = serializers.SerializerMethodField()
    total_time_spent = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'user_type', 'login_count', 'total_time_spent', 'is_online', 'current_session_duration']

    def get_is_online(self, obj):
        return obj.is_online()

    def get_current_session_duration(self, obj):
        if obj.is_online():
            return timezone.now() - obj.last_login_time
        return None

    def get_total_time_spent(self, obj):
        total_time_spent = obj.total_time
        if obj.is_online():
            total_time_spent += timezone.now() - obj.last_login_time
        return total_time_spent
