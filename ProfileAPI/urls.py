from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, sync_firebase_user

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    # Firebase sync user view for authenticating and linking Firebase users
    path('sync-firebase-user/', sync_firebase_user, name='sync_firebase_user'),
    
    # Include the router's URLs for profile-related API endpoints
    path('', include(router.urls)),
]
