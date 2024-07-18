from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, routers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

class UserApi(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'user_id'

  def get_queryset(self):
    queryset = User.objects.all()
    user_id = self.request.query_params.get('user_id')
    if user_id is not None:
      queryset = queryset.filter(user_id=user_id)
    return queryset
  
  def create(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, user_id):
    user = User.objects.get(user_id=user_id)
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, user_id):
    user = User.objects.get(user_id=user_id)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class UserInformationApi(viewsets.ModelViewSet):
  queryset = UserInformation.objects.all()
  serializer_class = UserInformationSerializer
  lookup_field = 'user'

  def get_queryset(self):
    queryset = UserInformation.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = UserInformationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, user):
    user = UserInformation.objects.get(user=user)
    serializer = UserInformationSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, user):
    user = UserInformation.objects.get(user=user)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class UserFollowApi(viewsets.ModelViewSet):
  queryset = UserFollow.objects.all()
  serializer_class = UserFollowSerializer
  lookup_field = 'user'

  def get_queryset(self):
    queryset = UserFollow.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = UserFollowSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, user):
    user = UserFollow.objects.get(user=user)
    serializer = UserFollowSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, user):
    user = UserFollow.objects.get(user=user)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class UserFollowerApi(viewsets.ModelViewSet):
  queryset = UserFollower.objects.all()
  serializer_class = UserFollowerSerializer
  lookup_field = 'user'

  def get_queryset(self):
    queryset = UserFollower.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = UserFollowerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, user):
    user = UserFollower.objects.get(user=user)
    serializer = UserFollowerSerializer(user, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, user):
    user = UserFollower.objects.get(user=user)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class MusicApi(viewsets.ModelViewSet):
  queryset = Music.objects.all()
  serializer_class = MusicSerializer
  lookup_field = 'music_id'

  def get_queryset(self):
    queryset = Music.objects.all()
    music_id = self.request.query_params.get('music_id')
    if music_id is not None:
      queryset = queryset.filter(music_id=music_id)
    return queryset
  
  def create(self, request):
    serializer = MusicSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, music_id):
    music = Music.objects.get(music_id=music_id)
    serializer = MusicSerializer(music, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, music_id):
    music = Music.objects.get(music_id=music_id)
    music.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class MusicLikedApi(viewsets.ModelViewSet):
  queryset = MusicLiked.objects.all()
  serializer_class = MusicLikedSerializer

  def get_queryset(self):
    queryset = MusicLiked.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = MusicLikedSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    user = request.data.get('user')
    music = request.data.get('music')
    music_liked = MusicLiked.objects.get(user=user, music=music)
    music_liked.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class MusicCommentsApi(viewsets.ModelViewSet):
  queryset = MusicComments.objects.all()
  serializer_class = MusicCommentsSerializer

  def get_queryset(self):
    queryset = MusicComments.objects.all()
    music = self.request.query_params.get('music')
    if music is not None:
      queryset = queryset.filter(music=music)
    return queryset
  
  def create(self, request):
    serializer = MusicCommentsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    music = request.data.get('music')
    user = request.data.get('user')
    comment = request.data.get('comment')
    music_comment = MusicComments.objects.get(music=music, user=user, comment=comment)
    music_comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class MusicContributeApi(viewsets.ModelViewSet):
  queryset = MusicContribute.objects.all()
  serializer_class = MusicContributeSerializer

  def get_queryset(self):
    queryset = MusicContribute.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = MusicContributeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    music = request.data.get('music')
    user = request.data.get('user')
    music_contribute = MusicContribute.objects.get(music=music, user=user)
    music_contribute.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class PlaylistApi(viewsets.ModelViewSet):
  queryset = Playlist.objects.all()
  serializer_class = PlaylistSerializer
  lookup_field = 'playlist_id'

  def get_queryset(self):
    queryset = Playlist.objects.all()
    playlist_id = self.request.query_params.get('playlist_id')
    if playlist_id is not None:
      queryset = queryset.filter(playlist_id=playlist_id)
    return queryset
  
  def create(self, request):
    serializer = PlaylistSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def update(self, request, playlist_id):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    serializer = PlaylistSerializer(playlist, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request, playlist_id):
    playlist = Playlist.objects.get(playlist_id=playlist_id)
    playlist.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class PlaylistMusicApi(viewsets.ModelViewSet):
  queryset = PlaylistMusic.objects.all()
  serializer_class = PlaylistMusicSerializer

  def get_queryset(self):
    queryset = PlaylistMusic.objects.all()
    playlist = self.request.query_params.get('playlist')
    if playlist is not None:
      queryset = queryset.filter(playlist=playlist)
    return queryset
  
  def create(self, request):
    serializer = PlaylistMusicSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    music = request.data.get('music')
    playlist = request.data.get('playlist')
    playlist_music = PlaylistMusic.objects.get(music=music, playlist=playlist)
    playlist_music.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class PlaylistLikedApi(viewsets.ModelViewSet):
  queryset = PlaylistLiked.objects.all()
  serializer_class = PlaylistLikedSerializer

  def get_queryset(self):
    queryset = PlaylistLiked.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = PlaylistLikedSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    user = request.data.get('user')
    music = request.data.get('music')
    music_liked = PlaylistLiked.objects.get(user=user, music=music)
    music_liked.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class PlaylistContributeApi(viewsets.ModelViewSet):
  queryset = PlaylistContribute.objects.all()
  serializer_class = PlaylistContributeSerializer

  def get_queryset(self):
    queryset = PlaylistContribute.objects.all()
    user = self.request.query_params.get('user')
    if user is not None:
      queryset = queryset.filter(user=user)
    return queryset
  
  def create(self, request):
    serializer = PlaylistContributeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  def destroy(self, request):
    playlist = request.data.get('playlist')
    user = request.data.get('user')
    playlist_contribute = PlaylistContribute.objects.get(playlist=playlist, user=user)
    playlist_contribute.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET'])
def music_list(request):
  if request.method == 'GET':
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def playlist_list(request):
  if request.method == 'GET':
    playlists = Playlist.objects.all()
    serializer = PlaylistSerializer(playlists, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def user_list(request):
  if request.method == 'GET':
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def user_follow_list(request):
  if request.method == 'GET':
    user_follows = UserFollow.objects.all()
    serializer = UserFollowSerializer(user_follows, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def user_follower_list(request):
  if request.method == 'GET':
    user_followers = UserFollower.objects.all()
    serializer = UserFollowerSerializer(user_followers, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def music_liked_list(request):
  if request.method == 'GET':
    music_likeds = MusicLiked.objects.all()
    serializer = MusicLikedSerializer(music_likeds, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def music_comments_list(request):
  if request.method == 'GET':
    music_comments = MusicComments.objects.all()
    serializer = MusicCommentsSerializer(music_comments, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def music_contribute_list(request):
  if request.method == 'GET':
    music_contributes = MusicContribute.objects.all()
    serializer = MusicContributeSerializer(music_contributes, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def playlist_music_list(request):
  if request.method == 'GET':
    playlist_musics = PlaylistMusic.objects.all()
    serializer = PlaylistMusicSerializer(playlist_musics, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def playlist_liked_list(request):
  if request.method == 'GET':
    playlist_likeds = PlaylistLiked.objects.all()
    serializer = PlaylistLikedSerializer(playlist_likeds, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def playlist_contribute_list(request):
  if request.method == 'GET':
    playlist_contributes = PlaylistContribute.objects.all()
    serializer = PlaylistContributeSerializer(playlist_contributes, many=True)
    return Response(serializer.data)
  
@api_view(['GET'])
def user_information_list(request):
  if request.method == 'GET':
    user_informations = UserInformation.objects.all()
    serializer = UserInformationSerializer(user_informations, many=True)
    return Response(serializer.data)
  
@api_view(['POST'])
def music_liked_create(request):
  if request.method == 'POST':
    serializer = MusicLikedSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def music_comments_create(request):
  if request.method == 'POST':
    serializer = MusicCommentsSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def music_contribute_create(request):
  if request.method == 'POST':
    serializer = MusicContributeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def playlist_music_create(request):
  if request.method == 'POST':
    serializer = PlaylistMusicSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def playlist_liked_create(request):
  if request.method == 'POST':
    serializer = PlaylistLikedSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def playlist_contribute_create(request):
  if request.method == 'POST':
    serializer = PlaylistContributeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def music_detail(request, music_id):
  music = get_object_or_404(Music, music_id=music_id)
  serializer = MusicSerializer(music)
  return Response(serializer.data)

@api_view(['GET'])
def playlist_detail(request, playlist_id):
  playlist = get_object_or_404(Playlist, playlist_id=playlist_id)
  serializer = PlaylistSerializer(playlist)
  return Response(serializer.data)

@api_view(['GET'])
def user_detail(request, user_id):
  user = get_object_or_404(User, user_id=user_id)
  serializer = UserSerializer(user)
  return Response(serializer.data)

@api_view(['GET'])
def user_follow_detail(request, user):
  user_follow = get_object_or_404(UserFollow, user=user)
  serializer = UserFollowSerializer(user_follow)
  return Response(serializer.data)

@api_view(['GET'])
def user_follower_detail(request, user):
  user_follower = get_object_or_404(UserFollower, user=user)
  serializer = UserFollowerSerializer(user_follower)
  return Response(serializer.data)

@api_view(['GET'])
def music_liked_detail(request, user, music):
  music_liked = get_object_or_404(MusicLiked, user=user, music=music)
  serializer = MusicLikedSerializer(music_liked)
  return Response(serializer.data)

@api_view(['GET'])
def music_comments_detail(request, user, music):
  music_comments = get_object_or_404(MusicComments, user=user, music=music)
  serializer = MusicCommentsSerializer(music_comments)
  return Response(serializer.data)

@api_view(['GET'])
def music_contribute_detail(request, user, music):
  music_contribute = get_object_or_404(MusicContribute, user=user, music=music)
  serializer = MusicContributeSerializer(music_contribute)
  return Response(serializer.data)

@api_view(['GET'])
def playlist_music_detail(request, music, playlist):
  playlist_music = get_object_or_404(PlaylistMusic, music=music, playlist=playlist)
  serializer = PlaylistMusicSerializer(playlist_music)
  return Response(serializer.data)

@api_view(['GET'])
def playlist_liked_detail(request, user, music):
  playlist_liked = get_object_or_404(PlaylistLiked, user=user, music=music)
  serializer = PlaylistLikedSerializer(playlist_liked)
  return Response(serializer.data)

@api_view(['GET'])
def playlist_contribute_detail(request, user, playlist):
  playlist_contribute = get_object_or_404(PlaylistContribute, user=user, playlist=playlist)
  serializer = PlaylistContributeSerializer(playlist_contribute)
  return Response(serializer.data)

@api_view(['GET'])
def user_information_detail(request, user):
  user_information = get_object_or_404(UserInformation, user=user)
  serializer = UserInformationSerializer(user_information)
  return Response(serializer.data)

@api_view(['PUT'])
def music_update(request, music_id):
  music = get_object_or_404(Music, music_id=music_id)
  serializer = MusicSerializer(music, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def playlist_update(request, playlist_id):
  playlist = get_object_or_404(Playlist, playlist_id=playlist_id)
  serializer = PlaylistSerializer(playlist, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_update(request, user_id):
  user = get_object_or_404(User, user_id=user_id)
  serializer = UserSerializer(user, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_follow_update(request, user):
  user_follow = get_object_or_404(UserFollow, user=user)
  serializer = UserFollowSerializer(user_follow, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_follower_update(request, user):
  user_follower = get_object_or_404(UserFollower, user=user)
  serializer = UserFollowerSerializer(user_follower, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def music_liked_update(request, user, music):
  music_liked = get_object_or_404(MusicLiked, user=user, music=music)
  serializer = MusicLikedSerializer(music_liked, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def music_comments_update(request, user, music):
  music_comments = get_object_or_404(MusicComments, user=user, music=music)
  serializer = MusicCommentsSerializer(music_comments, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def music_contribute_update(request, user, music):
  music_contribute = get_object_or_404(MusicContribute, user=user, music=music)
  serializer = MusicContributeSerializer(music_contribute, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def playlist_music_update(request, music, playlist):
  playlist_music = get_object_or_404(PlaylistMusic, music=music, playlist=playlist)
  serializer = PlaylistMusicSerializer(playlist_music, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def playlist_liked_update(request, user, music):
  playlist_liked = get_object_or_404(PlaylistLiked, user=user, music=music)
  serializer = PlaylistLikedSerializer(playlist_liked, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def playlist_contribute_update(request, user, playlist):
  playlist_contribute = get_object_or_404(PlaylistContribute, user=user, playlist=playlist)
  serializer = PlaylistContributeSerializer(playlist_contribute, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def user_information_update(request, user):
  user_information = get_object_or_404(UserInformation, user=user)
  serializer = UserInformationSerializer(user_information, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def music_delete(request, music_id):
  music = get_object_or_404(Music, music_id=music_id)
  music.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def playlist_delete(request, playlist_id):
  playlist = get_object_or_404(Playlist, playlist_id=playlist_id)
  playlist.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def user_delete(request, user_id):
  user = get_object_or_404(User, user_id=user_id)
  user.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def user_follow_delete(request, user):
  user_follow = get_object_or_404(UserFollow, user=user)
  user_follow.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def user_follower_delete(request, user):
  user_follower = get_object_or_404(UserFollower, user=user)
  user_follower.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def music_liked_delete(request, user, music):
  music_liked = get_object_or_404(MusicLiked, user=user, music=music)
  music_liked.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def music_comments_delete(request, user, music):
  music_comments = get_object_or_404(MusicComments, user=user, music=music)
  music_comments.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def music_contribute_delete(request, user, music):
  music_contribute = get_object_or_404(MusicContribute, user=user, music=music)
  music_contribute.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def playlist_music_delete(request, music, playlist):
  playlist_music = get_object_or_404(PlaylistMusic, music=music, playlist=playlist)
  playlist_music.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def playlist_liked_delete(request, user, music):
  playlist_liked = get_object_or_404(PlaylistLiked, user=user, music=music)
  playlist_liked.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def playlist_contribute_delete(request, user, playlist):
  playlist_contribute = get_object_or_404(PlaylistContribute, user=user, playlist=playlist)
  playlist_contribute.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def user_information_delete(request, user):
  user_information = get_object_or_404(UserInformation, user=user)
  user_information.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

# Path: myumyuWebSite/backend/api/urls.py
# Compare this snippet from myumyuWebSite/backend/api/urls.py:
# 
# from django.urls import path
# from rest_framework import routers
# from .views import *
#
# router = routers.DefaultRouter()
# router.register('user', UserViewSet)
# router.register('user_information', UserInformationViewSet)
# router.register('user_follow', UserFollowViewSet)
# router.register('user_follower', UserFollowerViewSet)
# router.register('music', MusicViewSet)
# router.register('music_liked', MusicLikedViewSet)
# router.register('music_comments', MusicCommentsViewSet)
# router.register('music_contribute', MusicContributeViewSet)
# router.register('playlist', PlaylistViewSet)

# urlpatterns = router.urls
# urlpatterns += [
#   path('music_list/', music_list),
#   path('playlist_list/', playlist_list),
#   path('user_list/', user_list),
#   path('user_follow_list/', user_follow_list),
#   path('user_follower_list/', user_follower_list),
#   path('music_liked_list/', music_liked_list),
#   path('music_comments_list/', music_comments_list),
#   path('music_contribute_list/', music_contribute_list),
#   path('playlist_music_list/', playlist_music_list),
#   path('playlist_liked_list/', playlist_liked_list),
#   path('playlist_contribute_list/', playlist_contribute_list),
#   path('user_information_list/', user_information_list),
#   path('music_liked_create/', music_liked_create),
#   path('music_comments_create/', music_comments_create),
#   path('music_contribute_create/', music_contribute_create),
#   path('playlist_music_create/', playlist_music_create),
#   path('playlist_liked_create/', playlist_liked_create),
#   path('playlist_contribute_create/', playlist_contribute_create),
#   path('music_detail/<str:music_id>/', music_detail),
#   path('playlist_detail/<str:playlist_id>/', playlist_detail),
#   path('user_detail/<str:user_id>/', user_detail),
#   path('user_follow_detail/<str:user>/', user_follow_detail),
#   path('user_follower_detail/<str:user>/', user_follower_detail),
#   path('music_liked_detail/<str:user>/<int:music>/', music_liked_detail),
#   path('music_comments_detail/<str:user>/<int:music>/', music_comments_detail),
#   path('music_contribute_detail/<str:user>/<int:music>/', music_contribute_detail),
#   path('playlist_music_detail/<int:music>/<int:playlist>/', playlist_music_detail),
#   path('playlist_liked_detail/<str:user>/<int:music>/', playlist_liked_detail),
#   path('playlist_contribute_detail/<str:user>/<int:playlist>/', playlist_contribute_detail),
#   path('user_information_detail/<str:user>/', user_information_detail),
#   path('music_update/<str:music_id>/', music_update),
#   path('playlist_update/<str:playlist_id>/', playlist_update),
#   path('user_update/<str:user_id>/', user_update),
#   path('user_follow_update/<str:user>/', user_follow_update),
#   path('user_follower_update/<str:user>/', user_follower_update),
#   path('music_liked_update/<str:user>/<int:music>/', music_liked_update),
#   path('music_comments_update/<str:user>/<int:music>/', music_comments_update),
#   path('music_contribute_update/<str:user>/<int:music>/', music_contribute_update),
#   path('playlist_music_update/<int:music>/<int:playlist>/', playlist_music_update),
#   path('playlist_liked_update/<str:user>/<int:music>/', playlist_liked_update),
#   path('playlist_contribute_update/<str:user>/<int:playlist>/', playlist_contribute_update),
#   path('user_information_update/<str:user>/', user_information_update),
#   path('music_delete/<str:music_id>/', music_delete),
#   path('playlist_delete/<str:playlist_id>/', playlist_delete),
#   path('user_delete/<str:user_id>/', user_delete),
#   path('user_follow_delete/<str:user>/', user_follow_delete),
#   path('user_follower_delete/<str:user>/', user_follower_delete),
#   path('music_liked_delete/<str:user>/<int:music>/', music_liked_delete),
#   path('music_comments_delete/<str:user>/<int:music>/', music_comments_delete),
#   path('music_contribute_delete/<str:user>/<int:music>/', music_contribute_delete),
#   path('playlist_music_delete/<int:music>/<int:playlist>/', playlist_music_delete),
#   path('playlist_liked_delete/<str:user>/<int:music>/', playlist_liked_delete),
#   path('playlist_contribute_delete/<str:user>/<int:playlist>/', playlist_contribute_delete),
#   path('user_information_delete/<str:user>/', user_information_delete),
# ] 
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('user', UserApi)
router.register('user_information', UserInformationApi)
router.register('user_follow', UserFollowApi)
router.register('user_follower', UserFollowerApi)
router.register('music', MusicApi)
router.register('music_liked', MusicLikedApi)
router.register('music_comments', MusicCommentsApi)
router.register('music_contribute', MusicContributeApi)
router.register('playlist', PlaylistApi)

urlpatterns = router.urls

urlpatterns += [

  path('music_list/', music_list),
  path('playlist_list/', playlist_list),
  path('user_list/', user_list),
  path('user_follow_list/', user_follow_list),
  path('user_follower_list/', user_follower_list),
  path('music_liked_list/', music_liked_list),
  path('music_comments_list/', music_comments_list),
  path('music_contribute_list/', music_contribute_list),
  path('playlist_music_list/', playlist_music_list),
  path('playlist_liked_list/', playlist_liked_list),
  path('playlist_contribute_list/', playlist_contribute_list),
  path('user_information_list/', user_information_list),
  path('music_liked_create/', music_liked_create),
  path('music_comments_create/', music_comments_create),
  path('music_contribute_create/', music_contribute_create),
  path('playlist_music_create/', playlist_music_create),
  path('playlist_liked_create/', playlist_liked_create),
  path('playlist_contribute_create/', playlist_contribute_create),
  path('music_detail/<str:music_id>/', music_detail),
  path('playlist_detail/<str:playlist_id>/', playlist_detail),
  path('user_detail/<str:user_id>/', user_detail),
  path('user_follow_detail/<str:user>/', user_follow_detail),
  path('user_follower_detail/<str:user>/', user_follower_detail),
  path('music_liked_detail/<str:user>/<int:music>/', music_liked_detail),
  path('music_comments_detail/<str:user>/<int:music>/', music_comments_detail),
  path('music_contribute_detail/<str:user>/<int:music>/', music_contribute_detail),
  path('playlist_music_detail/<int:music>/<int:playlist>/', playlist_music_detail),
  path('playlist_liked_detail/<str:user>/<int:music>/', playlist_liked_detail),
  path('playlist_contribute_detail/<str:user>/<int:playlist>/', playlist_contribute_detail),
  path('user_information_detail/<str:user>/', user_information_detail),
  path('music_update/<str:music_id>/', music_update),
  path('playlist_update/<str:playlist_id>/', playlist_update),
  path('user_update/<str:user_id>/', user_update),
  path('user_follow_update/<str:user>/', user_follow_update),
  path('user_follower_update/<str:user>/', user_follower_update),
  path('music_liked_update/<str:user>/<int:music>/', music_liked_update),
  path('music_comments_update/<str:user>/<int:music>/', music_comments_update),
  path('music_contribute_update/<str:user>/<int:music>/', music_contribute_update),
  path('playlist_music_update/<int:music>/<int:playlist>/', playlist_music_update),
  path('playlist_liked_update/<str:user>/<int:music>/', playlist_liked_update),
  path('playlist_contribute_update/<str:user>/<int:playlist>/', playlist_contribute_update),
  path('user_information_update/<str:user>/', user_information_update),
  path('music_delete/<str:music_id>/', music_delete),
  path('playlist_delete/<str:playlist_id>/', playlist_delete),
  path('user_delete/<str:user_id>/', user_delete),
  path('user_follow_delete/<str:user>/', user_follow_delete),
  path('user_follower_delete/<str:user>/', user_follower_delete),
  path('music_liked_delete/<str:user>/<int:music>/', music_liked_delete),
  path('music_comments_delete/<str:user>/<int:music>/', music_comments_delete),
  path('music_contribute_delete/<str:user>/<int:music>/', music_contribute_delete),
  path('playlist_music_delete/<int:music>/<int:playlist>/', playlist_music_delete),
  path('playlist_liked_delete/<str:user>/<int:music>/', playlist_liked_delete),
  path('playlist_contribute_delete/<str:user>/<int:playlist>/', playlist_contribute_delete),
  path('user_information_delete/<str:user>/', user_information_delete),

]

