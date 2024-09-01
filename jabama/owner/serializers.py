from .models import Owner
from rest_framework import serializers
from django.contrib.auth.models import User

class OwnerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Owner
        fields = ['id', 'username', 'email', 'bio', 'money_wallet']

class OwnerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = Owner
        fields = ['id', 'username', 'email', 'password', 'password_confirmation']
    
    def validate(self, data):
        if data['password']!= data['password_confirmation']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

