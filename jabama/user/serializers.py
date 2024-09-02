from .models import Customer
from rest_framework import serializers
from django.contrib.auth.models import User
from owner.models import Owner

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'bio', 'money_wallet', 'is_owner']

class UserProfileRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirmation', 'first_name', 'last_name']
    
    def validate(self, data):
        if data['password']!= data['password_confirmation']:
            raise serializers.ValidationError('Passwords do not match.')
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], first_name=validated_data['first_name'], last_name=validated_data['last_name'])
        return user

class OwnerSerializer(serializers.ModelSerializer):
    customer_id = serializers.PrimaryKeyRelatedField(queryset = Customer.objects.all(), source = 'customer')

    class Meta:
        model = Owner
        fields = ['id', 'customer_id']


    
            