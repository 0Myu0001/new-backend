from django.shortcuts import render
from rest_framework import viewsets, routers
from .models import User
from .models import User_Strict_Information
from .models import User_Experience
from .models import Playlist
from .models import Notification
from .models import Post
from .models import Post_Comments
from .models import Post_Detail
from .serializers import UserSerializer
from .serializers import User_Strict_InformationSerializer
from .serializers import User_ExperienceSerializer
from .serializers import PlaylistSerializer
from .serializers import NotificationSerializer
from .serializers import PostSerializer
from .serializers import Post_CommentsSerializer
from .serializers import Post_DetailSerializer

# Create your views here.

class UserApi (viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get_queryset(self):
    queryset = User.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset
  
class PostApi (viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def get_queryset(self):
    queryset = Post.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset
  
class User_Strict_InformationApi (viewsets.ModelViewSet):
  queryset = User_Strict_Information.objects.all()
  serializer_class = User_Strict_InformationSerializer

  def get_queryset(self):
    queryset = User_Strict_Information.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset

class User_ExperienceApi (viewsets.ModelViewSet):
  queryset = User_Experience.objects.all()
  serializer_class = User_ExperienceSerializer

  def get_queryset(self):
    queryset = User_Experience.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset

class PlaylistApi (viewsets.ModelViewSet):
  queryset = Playlist.objects.all()
  serializer_class = PlaylistSerializer

  def get_queryset(self):
    queryset = Playlist.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset
  
class NotificationApi (viewsets.ModelViewSet):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer

  def get_queryset(self):
    queryset = Notification.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset

class Post_CommentsApi (viewsets.ModelViewSet):
  queryset = Post_Comments.objects.all()
  serializer_class = Post_CommentsSerializer

  def get_queryset(self):
    queryset = Post_Comments.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset

class Post_DetailApi (viewsets.ModelViewSet):
  queryset = Post_Detail.objects.all()
  serializer_class = Post_DetailSerializer

  def get_queryset(self):
    queryset = Post_Detail.objects.all()
    L_id = self.request.query_params.get('id', None)

    if L_id:
      queryset = queryset.filter(user_id=L_id)
    return queryset
  
router = routers.DefaultRouter()
router.register(r'user', UserApi)
router.register(r'post', PostApi)
router.register(r'user_strict_information', User_Strict_InformationApi)
router.register(r'user_experience', User_ExperienceApi)
router.register(r'playlist', PlaylistApi)
router.register(r'notification', NotificationApi)
router.register(r'post_comments', Post_CommentsApi)
router.register(r'post_detail', Post_DetailApi)

