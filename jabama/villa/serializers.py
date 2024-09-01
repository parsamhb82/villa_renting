from .models import Villa , Comment , Rate
from rest_framework import serializers
from django.contrib.auth.models import User

class VillaSerializer(serializers.ModelSerializer):
        class Meta:
            model = Villa
            fields ='__all__'


    

