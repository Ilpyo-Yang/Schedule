from rest_framework import viewsets
from rest_framework import permissions
from .serializers import TodoSerializer, CommentSerializer, UserSerializer
from .models import Todo, Comment, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("username")
    serializr_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("create_at")
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("create_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
