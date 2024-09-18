from . import views
# from register.views import PostListView
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [  
    path("", views.home, name="home"),
    path("register/", views.register, name="register"), 
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("master/", views.master, name="master"), 
    path("newtasks/", views.taskss, name="tasks"),
    path("tasks/", views.taskview, name="tasksss"),
    path("logout/", views.logout, name="logout"),
]  