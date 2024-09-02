
from django.urls import path
from .views import (Login,
                    Refresh,
                    UserProfileList,
                    UserProfileView,
                    )

urlpatterns = [
        path("create_owner/", views.CreateOwnerView.as_view())
]
