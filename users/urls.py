from django.urls import path
from .views import (
    PublicAPIView, 
    ProtectedAPIView, 
    TelegramUserListView,
    RegisterAPIView
)

urlpatterns = [
    path('public/', PublicAPIView.as_view(), name='public-api'),
    path('protected/', ProtectedAPIView.as_view(), name='protected-api'),
    path('telegram-users/', TelegramUserListView.as_view(), name='telegram-users'),
    path('register/', RegisterAPIView.as_view(), name='register'),
]