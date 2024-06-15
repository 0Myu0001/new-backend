from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, routers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class UserApi (viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = User.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class User_FollowersApi (viewsets.ModelViewSet):
  queryset = User_Followers.objects.all()
  serializer_class = User_FollowersSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = User_Followers.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class User_FollowingsApi (viewsets.ModelViewSet):
  queryset = User_Followings.objects.all()
  serializer_class = User_FollowingsSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = User_Followings.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class User_Strict_InformationApi (viewsets.ModelViewSet):
  queryset = User_Strict_Information.objects.all()
  serializer_class = User_Strict_InformationSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = User_Strict_Information.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class PostApi (viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  def get_queryset(self):
    queryset = Post.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset
  
class Post_CommentsApi (viewsets.ModelViewSet):
  queryset = Post_Comments.objects.all()
  serializer_class = Post_CommentsSerializer
  lookup_field = 'post_id'

  def get_queryset(self):
    queryset = Post_Comments.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset
  
class Post_LovedApi (viewsets.ModelViewSet):
  queryset = Post_Loved.objects.all()
  serializer_class = Post_LovedSerializer
  lookup_field = 'post_id'

  def get_queryset(self):
    queryset = Post_Loved.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class PlaylistApi (viewsets.ModelViewSet):
  queryset = Playlist.objects.all()
  serializer_class = PlaylistSerializer
  lookup_field = 'playlist_id'

  def get_queryset(self):
    queryset = Playlist.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class PlaylistPostsApi (viewsets.ModelViewSet):
  queryset = PlaylistPosts.objects.all()
  serializer_class = PlaylistPostsSerializer

  def get_queryset(self):
    queryset = PlaylistPosts.objects.all()
    playlist_id = self.request.query_params.get('playlist_id')
    if playlist_id is not None:
      queryset = queryset.filter(playlist_id=playlist_id)
    return queryset

class Playlist_CommentsApi (viewsets.ModelViewSet):
  queryset = Playlist_Comments.objects.all()
  serializer_class = Playlist_CommentsSerializer
  lookup_field = 'playlist_id'

  def get_queryset(self):
    queryset = Playlist_Comments.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset

class Playlist_LovedApi (viewsets.ModelViewSet):
  queryset = Playlist_Loved.objects.all()
  serializer_class = Playlist_LovedSerializer
  lookup_field = 'playlist_id'

  def get_queryset(self):
    queryset = Playlist_Loved.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset
  
class NotificationApi (viewsets.ModelViewSet):
  queryset = Notification.objects.all()
  serializer_class = NotificationSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = Notification.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset
  
def create_user(request):
  if request.method == 'POST':
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      # データをセッションに保存
      request.session['user_data'] = serializer.validated_data
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@login_required
def complete_registration(request):
  # セッションからデータを取得
  user_data = request.session.get('user_data')
  if user_data:
    # データをモデルに保存
    User.objects.create(**user_data)
    # セッションからデータを削除
    del request.session['user_data']
    return Response({'status': 'Registration completed'}, status=status.HTTP_201_CREATED)
  return Response({'status': 'No data found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_model(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
router = routers.DefaultRouter()
router.register(r'user', UserApi)
router.register(r'user_followers', User_FollowersApi)
router.register(r'user_followings', User_FollowingsApi)
router.register(r'user_strict_information', User_Strict_InformationApi)
router.register(r'post', PostApi)
router.register(r'post_comments', Post_CommentsApi)
router.register(r'post_loved', Post_LovedApi)
router.register(r'playlist', PlaylistApi)
router.register(r'playlist_comments', Playlist_CommentsApi)
router.register(r'playlist_loved', Playlist_LovedApi)
router.register(r'notification', NotificationApi)
router.register(r'playlist_posts', PlaylistPostsApi)
