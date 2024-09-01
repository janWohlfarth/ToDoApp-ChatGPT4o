from rest_framework import viewsets, permissions
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.authentication import TokenAuthentication

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Todo.objects.filter(user=self.request.user)
        return Todo.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
