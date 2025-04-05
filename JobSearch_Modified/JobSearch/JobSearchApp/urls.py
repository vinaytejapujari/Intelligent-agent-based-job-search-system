from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),	      
			path("Login.html", views.Login, name="Login"),
			path("Signup.html", views.Signup, name="Signup"),
			path("SignupAction", views.SignupAction, name="SignupAction"),	
			path("LoginAction", views.LoginAction, name="LoginAction"),	
			path("PostJob.html", views.PostJob, name="PostJob"),
			path("PostJobAction", views.PostJobAction, name="PostJobAction"),
			path("ActivateJob", views.ActivateJob, name="ActivateJob"),
			path("SearchJob.html", views.SearchJob, name="SearchJob"),
			path("SearchJobAction", views.SearchJobAction, name="SearchJobAction"),
			path("Activate", views.Activate, name="Activate"),
]