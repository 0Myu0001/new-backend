from django.urls import path
from .views import *
from . import views

urlpatterns = [
  path('', views.UserApi.as_view({'get': 'list', 'post': 'create'})),
  path('api/user/<str:pk>/', UserApi.as_view({'get': 'retrieve'})),
  path('api/post/<str:pk>/', PostApi.as_view({'get': 'retrieve'})),
  path('api/user_strict_information/<str:pk>/', User_Strict_InformationApi.as_view({'get': 'retrieve'})),
]
