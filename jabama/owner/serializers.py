from .models import Owner
from rest_framework import serializers
from django.contrib.auth.models import User

class OwnerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Owner
            fields ='__all__'

