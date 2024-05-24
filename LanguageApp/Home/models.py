from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=100,default="")
    Email=models.EmailField(max_length=100)
    language_level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    language_level = models.CharField(max_length=25, choices=language_level_choices)
    
    # New fields for progress tracking and personalization
    completed_lessons = models.ManyToManyField('Lesson', blank=True, related_name="You have completed all this lessons")
    favorite_language = models.ForeignKey('Language', null=True, blank=True, on_delete=models.PROTECT)