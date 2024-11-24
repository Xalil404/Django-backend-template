from rest_framework import viewsets, permissions
from .models import Profile
from .serializers import ProfileSerializer
from .utils import verify_firebase_token  # Import the function from utils.py

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Verify Firebase token (this might not be necessary if you're already verifying in authentication layer)
        firebase_token = self.request.headers.get('Authorization', None)
        if firebase_token:
            decoded_token = verify_firebase_token(firebase_token)  # Verify token here
            # You can use decoded_token data (like UID) to filter or handle user-specific logic

        # Limit access to only the profile of the authenticated user
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Verify the Firebase token here to create the profile
        firebase_token = self.request.headers.get('Authorization', None)
        if firebase_token:
            decoded_token = verify_firebase_token(firebase_token)  # Verify token before creating

        # Create the profile associated with the authenticated user
        serializer.save(user=self.request.user)
