# profile/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # To select existing users

    class Meta:
        model = Profile
        fields = ['id', 'user', 'avatar', 'bio', 'location', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
