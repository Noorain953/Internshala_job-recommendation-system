from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    skills = models.JSONField()  # Store skills as a list of strings
    experience_level = models.CharField(max_length=50, choices=[("Junior", "Junior"), ("Intermediate", "Intermediate"), ("Senior", "Senior")])
    preferences = models.JSONField()  # Store preferences as JSON object

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    required_skills = models.JSONField()  # Store required skills as a list of strings
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[("Full-Time", "Full-Time"), ("Part-Time", "Part-Time"), ("Contract", "Contract")])
    experience_level = models.CharField(max_length=50, choices=[("Junior", "Junior"), ("Intermediate", "Intermediate"), ("Senior", "Senior")])

    def __str__(self):
        return self.job_title
