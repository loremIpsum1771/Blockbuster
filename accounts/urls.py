from django.contrib import admin
from django.urls import path,include
import os

from .views import(
    UserCreate,

)

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
   # path('api/register/',UserCreateAPIView.as_view() ,name='register'),
   #path('api-auth/',include('rest_framework.urls')),
   #path('api/token/',TokenObtainPairView.as_view()),
   #path('api/token/refresh/',TokenRefreshView.as_view()),
   path('api/users', UserCreate.as_view(), name='account-create'),


    ]
