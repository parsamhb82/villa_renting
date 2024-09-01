from .models import Customer
from rest_framework import serializers
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'bio', 'money_wallet']

class UserProfileRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'password', 'password_confirmation']
    
    def validate(self, data):
        if data['password']!= data['password_confirmation']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class CustomerToOwner(serializers.ModelSerializer):
    if Customer.is_owner == 'True':
        class Meta:
            model = Customer
            fields ='__all__'
    
            