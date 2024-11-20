from django.urls import path
from .views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
]
