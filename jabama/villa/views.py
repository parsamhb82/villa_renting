from django.shortcuts import render
from .serializers import VillaSerializer
from .models import Villa , Comment , Rate
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from user.models import Customer
from django.db import transaction
from owner.models import Owner

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass


def Calculate_rate(request):
    pass

class VillaView(ListAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer


class VillaDetails(RetrieveAPIView):
    queryset = Villa.objects.all()
    serializer_class = VillaSerializer
    
def Sale(request):
    if Customer.money_wallet >= Villa.price:
        with transaction.atomic():
            Customer.money_wallet -= Villa.price
            Owner.user -= Villa.price
        
    pass
            
            
# Create your views here.
