from django.shortcuts import render,redirect
from rest_framework import generics, viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Firm
from .serializers import UserSerializer, FirmSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API for viewing/updating/deleting users.
    Admin can access all, regular user only their own.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()  # admin sees all
        return User.objects.filter(id=user.id)  # user sees only self

    def get_object(self):
        user = self.request.user
        if user.is_superuser:
            return super().get_object()  # object by pk for admin
        return user  # always return self for normal user

class FirmViewSet(viewsets.ModelViewSet):
    """
    API for firm creation and management.
    Admin can access all; regular users only their firms.
    """
    serializer_class = FirmSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Firm.objects.all()  # admin sees all
        return Firm.objects.filter(user=user)  # user sees only own firms

    def perform_create(self, serializer):
        # Automatically assign the firm to the logged-in user
        serializer.save(user=self.request.user)

def register_page(request):
    return render(request, "core/register.html")

def login_page(request):
    return render(request, "core/login.html")

def dashboard_page(request):
    if not request.user.is_authenticated:
        return redirect('login-page')
    return render(request, "core/dashboard.html")
