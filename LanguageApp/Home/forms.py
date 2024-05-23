from .models import LessonTag
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from .models import UserProfile, Lesson, Language, LessonTag, UserLanguage

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ('username', 'first_name', 
                  'last_name','email',
                  'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ("full_name","lessons_completed","lessons_in_progress",        "favorite_languages","languages_level","languages_learning")
        
class LessonsForm(forms.ModelForm):
    
    class Meta:
        model = Lesson
        fields = ("title","content","language","lesson_tags","lesson_level","lesson_duration")

    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter the lesson title'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Enter the lesson content'}))