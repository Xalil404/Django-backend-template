from django.shortcuts import render

# ProfileAPI/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
import firebase_admin
from firebase_admin import auth, credentials
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

# Initialize Firebase Admin if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CREDENTIALS_PATH)
    firebase_admin.initialize_app(cred)

# ProfileViewSet for CRUD operations on profiles
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """Get profiles only for the authenticated user."""
        return Profile.objects.filter(user=self.request.user)

# Firebase sync view to handle user creation or updating from Firebase token
@csrf_exempt
def sync_firebase_user(request):
    if request.method == 'POST':
        token = request.POST.get('idToken')

        try:
            # Verify the Firebase token
            decoded_token = auth.verify_id_token(token)
            firebase_uid = decoded_token['uid']
            email = decoded_token['email']
            name = decoded_token.get('name', '')

            # Create or get the user in Django
            User = get_user_model()
            user, created = User.objects.get_or_create(username=firebase_uid, defaults={'email': email})

            # Create or update the profile for the user
            profile, created = Profile.objects.get_or_create(user=user)
            if created:
                profile.bio = f"Firebase user: {name}"
                profile.save()

            return JsonResponse({'status': 'success', 'user': {'username': user.username, 'email': user.email}}, status=200)

        except auth.InvalidIdTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
