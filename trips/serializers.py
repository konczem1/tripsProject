from rest_framework import serializers
from .models import User, Photo


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'firstName', 'lastName', 'dateOfBirth', 'dateOfJoining', 'country', 'email', 'password')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'filename', 'latitude', 'longitude', 'owner')
