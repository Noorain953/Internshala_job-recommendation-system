from rest_framework import serializers
from .models import UserProfile, JobPosting

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'skills', 'experience_level', 'preferences']


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ['job_title', 'company', 'required_skills', 'location', 'job_type', 'experience_level']
