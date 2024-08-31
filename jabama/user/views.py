from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from user.serializers import UserProfileSerializer, UserProfileRegisterSerializer
from user.models import Customer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass

class UserProfileList(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileView(RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

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

        return JsonResponse({'message' : 'user registered successfuly'}, status = 201)


