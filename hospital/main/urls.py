from django.urls import path, include
from django.contrib import admin
from . import views

# app_name = 'main'
urlpatterns = [
  
#  path('login/', include('django.contrib.auth.urls')),
path('', views.homepage,name='homepage'),
path('home/', views.home,name='home'),
path('department/', views.department,name='department'),

 path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('login2/', views.loginPage2, name="login2"),  
 
	path('logout/', views.logoutUser, name="logout"),
	path('logout2/', views.logoutUser2, name="logout2"),
 
]