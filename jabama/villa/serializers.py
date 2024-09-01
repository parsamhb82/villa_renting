from .models import Villa , Comment , Rate, Rent
from rest_framework import serializers
from django.contrib.auth.models import User

class VillaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Villa
            fields ='__all__'

class CommentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields ='__all__'

class RateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Rate
            fields ='__all__'

class RentSerializer(serializers.ModelSerializer):
        class Meta:
            model = Rent
            fields ='__all__'


    

