from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework import generics, permissions


# List and Create Profiles
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create/view profiles

    def perform_create(self, serializer):
        # Automatically associate the profile with the logged-in user
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete Profile
class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view/update/delete profiles

