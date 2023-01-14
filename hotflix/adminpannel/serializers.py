from rest_framework import serializers
from .models import VideosDetails, UserDetails

class VideoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideosDetails
        fields = ('__all__')


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ('__all__')