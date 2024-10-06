from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserProfile, JobPosting
from .serializers import UserProfileSerializer, JobPostingSerializer
from django.db.models import Q

class UserProfileCreateView(APIView):
    def post(self, request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobRecommendationView(APIView):
    def get(self, request):
        user_profile_data = request.query_params
        user_profile_serializer = UserProfileSerializer(data=user_profile_data)
        
        if user_profile_serializer.is_valid():
            user_profile = user_profile_serializer.validated_data
            
            # Extract the user's preferences and skills
            user_skills = user_profile['skills']
            user_experience_level = user_profile['experience_level']
            user_preferences = user_profile['preferences']

            # Filter jobs based on skills, experience level, and preferences
            recommended_jobs = JobPosting.objects.filter(
                Q(required_skills__overlap=user_skills) & 
                Q(experience_level=user_experience_level) &
                Q(location__in=user_preferences['locations']) &
                Q(job_type=user_preferences['job_type'])
            )
            
            # Serialize and return the recommended jobs
            job_serializer = JobPostingSerializer(recommended_jobs, many=True)
            return Response(job_serializer.data)
        
        return Response(user_profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
