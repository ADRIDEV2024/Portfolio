from django.urls import path
from .import views

    urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path("logout/", views.logout, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("communityposts/", views.communityposts, name="communityposts"),
    path("update_profile/", views.updateprofile, name="updateprofile"),
    path("addlesson/", views.addlesson, name= "addlesson"),
    path("favorite_language/", views.favorite_language, name="select_favorite_language"),
    path("language/<int:language_id>/", views.language, name="language"),
    path("lessons_detail/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    ),
]
