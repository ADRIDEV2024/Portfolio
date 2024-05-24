from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("communityposts/", views.communityposts, name="communityposts"),
    path("updateprofile/", views.updateprofile, name="updateprofile"),
    path("addlesson/", views.addlesson, name= "addlesson"),
]