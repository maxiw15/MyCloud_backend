from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .models import File
from .serializers import UserSerializer, RegisterSerializer, FileSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class FileListView(generics.ListCreateAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return File.objects.all()
        return File.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return File.objects.all()
        return File.objects.filter(user=user)
