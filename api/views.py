from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, routers
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class UserApi(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def retrieve(self, request, pk=None):
    queryset = User.objects.filter(user_id=pk)
    user = get_object_or_404(queryset, user_id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
class PostApi (viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(post_id=pk)
    post = get_object_or_404(queryset, post_id=pk)
    serializer = PostSerializer(post)
    return Response(serializer.data)
  
class User_Strict_InformationApi (viewsets.ModelViewSet):
  queryset = User_Strict_Information.objects.all()
  serializer_class = User_Strict_InformationSerializer

  def retrieve(self, request, pk=None):
    queryset = User_Strict_Information.objects.filter(user_id=pk)
    user_strict_information = get_object_or_404(queryset, user_id=pk)
    serializer = User_Strict_InformationSerializer(user_strict_information)
    return Response(serializer.data)

class User_ExperienceApi (viewsets.ModelViewSet):
  queryset = User_Experience.objects.all()
  serializer_class = User_ExperienceSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(user_id=pk)
    user_experience = get_object_or_404(queryset, user_id=pk)
    serializer = User_ExperienceSerializer(user_experience)
    return Response(serializer.data)

class PlaylistApi (viewsets.ModelViewSet):
  queryset = Playlist.objects.all()
  serializer_class = PlaylistSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(playlist_id=pk)
    playlist = get_object_or_404(queryset, playlist_id=pk)
    serializer = PlaylistSerializer(playlist)
    return Response(serializer.data)
  
class NotificationApi (viewsets.ModelViewSet):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(notification_id=pk)
    notification = get_object_or_404(queryset, notification_id=pk)
    serializer = NotificationSerializer(notification)
    return Response(serializer.data)

class Post_CommentsApi (viewsets.ModelViewSet):
  queryset = Post_Comments.objects.all()
  serializer_class = Post_CommentsSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(post_id=pk)
    post = get_object_or_404(queryset, post_id=pk)
    serializer = Post_CommentsSerializer(post)
    return Response(serializer.data)

class Post_DetailApi (viewsets.ModelViewSet):
  queryset = Post_Detail.objects.all()
  serializer_class = Post_DetailSerializer

  def retrieve(self, request, pk=None):
    queryset = Post.objects.filter(post_id=pk)
    post = get_object_or_404(queryset, post_id=pk)
    serializer = Post_DetailSerializer(post)
    return Response(serializer.data)
  
router = routers.DefaultRouter()
router.register(r'user', UserApi)
router.register(r'post', PostApi)
router.register(r'user_strict_information', User_Strict_InformationApi)
router.register(r'user_experience', User_ExperienceApi)
router.register(r'playlist', PlaylistApi)
router.register(r'notification', NotificationApi)
router.register(r'post_comments', Post_CommentsApi)
router.register(r'post_detail', Post_DetailApi)
