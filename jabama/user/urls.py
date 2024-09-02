
from django.urls import path
from .views import (Login,
                    Refresh,
                    UserProfileList,
                    UserProfileView,
                    UserRegistrationView,
                    CreateOwnerView,
                    )

urlpatterns = [
        path("create_owner/", CreateOwnerView.as_view()),
        path("login/", Login.as_view()),
        path("refresh/", Refresh.as_view()),
        path("register/", UserRegistrationView.as_view()),
        path("profile/<int:pk/>", UserProfileView.as_view()),
        path("profile/list/", UserProfileList.as_view()),

]
