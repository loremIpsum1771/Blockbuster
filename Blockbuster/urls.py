"""Blockbuster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
import os
#from rest_framework_jwt.views import obtain_jwt_token

from bbster.views import(
    GenreListAPIView,
    MovieListAPIView,
    MovieDetailAPIView,
    MovieUpdateAPIView,
    MovieDestroyAPIView,
    MovieCreateAPIView
)

# from accounts.views import(
#     UserCreateAPIView,
# )

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('api/genre/',GenreListAPIView.as_view() ,name='genre'),
    path('api/movie/',MovieListAPIView.as_view() ,name='movielist'),
    path('api/movie/<int:pk>/',MovieDetailAPIView.as_view() ,name='moviedetails'),
    path('api/movie/edit/<int:pk>/',MovieUpdateAPIView.as_view() ,name='updatemovie'),
    path('api/movie/delete/<int:pk>/',MovieDestroyAPIView.as_view() ,name='destroymovie'),
    path('api/movie/create/',MovieCreateAPIView.as_view() ,name='createmovie'),
#    path('api/register/',UserCreateAPIView.as_view() ,name='register'),
 #    path('auth/login/', LoginView.as_view(), name="auth-login"),
    
    path('',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
     #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),

    
]
