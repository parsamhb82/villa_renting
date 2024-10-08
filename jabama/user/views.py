from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from user.serializers import UserProfileSerializer, UserProfileRegisterSerializer, OwnerSerializer
from user.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner, IsSuperUser
from rest_framework import status
class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class UserProfileList(ListAPIView):
    permission_classes = [IsSuperUser]
    queryset = Customer.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Customer.objects.filter(user=self.request.user)

class UserRegistrationView(CreateAPIView):
    serializer_class = UserProfileRegisterSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = self.get_serializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        profile_data = {
            'bio' : request.data.get('bio', ''),
            'money_wallet' : request.data.get('money_wallet', 0),
        }

        Customer.objects.create(user=user, **profile_data)

        return Response({'message' : 'user registered successfuly'}, status = status.HTTP_201_CREATED)



class CreateOwnerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.validated_data['customer']

            if customer.is_owner:
                return Response({'error' : 'customer is already an owner'}, status = status.HTTP_400_BAD_REQUEST)
            
            owner = serializer.save()

            owner.customer.is_owner = True
            customer.save()

            return JsonResponse({'message' : 'owner created successfuly'}, status = status.HTTP_201_CREATED)
        
        return JsonResponse({'error' : 'bad request'}, status = status.HTTP_400_BAD_REQUEST)



            

    





