from django.urls import path
from .views import UserRegistrationView, UserLoginView, TokenVerifyView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
