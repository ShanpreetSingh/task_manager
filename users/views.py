from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
from .serializers import UserSerializer, TelegramUserSerializer, RegisterSerializer
from .models import TelegramUser
from .tasks import send_welcome_email

class PublicAPIView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        return Response({"message": "Public endpoint - no authentication required"})

class ProtectedAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        return Response({"message": f"Protected endpoint - welcome {request.user.username}"})

class TelegramUserListView(generics.ListAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterAPIView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        # Create auth token
        token, created = Token.objects.get_or_create(user=user)
        
        # Send welcome email via Celery
        send_welcome_email.delay(user.id)
        
        # Login user (for web interface)
        login(request, user)
        
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key,
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)