from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class User_FollowersSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Followers
    fields = '__all__'

class User_FollowingsSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Followings
    fields = '__all__'

class User_Strict_InformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Strict_Information
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class Post_CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post_Comments
    fields = '__all__'

class Post_LovedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post_Loved
    fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist
    fields = '__all__'

class Playlist_CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist_Comments
    fields = '__all__'

class Playlist_LovedSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist_Loved
    fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = '__all__'

