from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter tasks to show only those of the logged-in user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the task
        serializer.save(user=self.request.user)
