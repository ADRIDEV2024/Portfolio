from .forms import FavoriteLanguageForm, LessonsForm, UserProfileForm
from django.contrib import auth, messages
from .models import UserProfile, Lesson, Language, UserLanguage, CommunityPost
from django.contrib.auth.views import LoginView
from .models import Lesson, UserProfile
from .forms import LessonTagForm, LanguageForm, SignUpForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

def index(request):

    return render(request, 'index.html')

def dashboard(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_languages = UserLanguage.objects.filter(user=request.user)
    community_posts = CommunityPost.objects.all()
    
    # Fetch completed lessons and favorite language
    completed_lessons = user_profile.lessons_completed.all()
    favorite_language = user_profile.favorite_language
    
    context = {
        'user_profile': user_profile,
        'user_languages': user_languages,
        'community_posts': community_posts,
        "completed_lessons": completed_lessons,
        "favorite_language": favorite_language
    }
    return render(request, "dashboard.html", context)

def communityposts(request):
    posts = CommunityPost.objects.all()
    return render(request, "community_posts.html", {"posts": posts})

def updateprofile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_languages = UserLanguage.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    # Redirect to the index page after succesfull form submission
        return redirect("index")
    else:
        form = UserProfileForm(instance=user_profile)
        context = {
            "form": form,
        }
        return render(request, "update_profile.html", context)
    
def addlesson(request):
    if request.method == 'POST':
        form = LessonsForm(request.POST)
        if form.is_valid():
            form.save()
     # Redirect to the lesson detail page after succesfull form submission
        return redirect("update_profile")
    else:
        form = LessonsForm()
        context = {
            "form": form,
        }
        return render(request, "add_lesson.html", context)
    
def create_community_post(request):
    if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       user = request.user
       CommunityPost.objects.create(user=user, title=title, content=content)
       
       return redirect("communityposts")
   
    return render(request, "create_community_post.html")
    
def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html')
        else:
            messages.info(request, "successfully")
                    
            return render(request, 'login.html')
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out")
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"], 
                                 password=request.POST["password"])
        if user is not None:
            user_profile = UserProfile.objects.get(user=user)
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')