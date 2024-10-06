from django.urls import path
from .views import UserProfileCreateView, JobRecommendationView

urlpatterns = [
    path('user-profiles/', UserProfileCreateView.as_view(), name='user-profile-create'),
    path('recommendations/', JobRecommendationView.as_view(), name='job-recommendations'),
]
