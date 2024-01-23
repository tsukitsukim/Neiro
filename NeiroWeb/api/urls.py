from django.urls import path, include
from .views import UserRegistrationAPIView

urlpatterns = [
    path('v1/auth/register/', UserRegistrationAPIView.as_view())
]
