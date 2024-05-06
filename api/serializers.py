from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class User_Strict_InformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Strict_Information
    fields = '__all__'

class User_ExperienceSerializer(serializers.ModelSerializer):
  class Meta:
    model = User_Experience
    fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist
    fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    fields = '__all__'

class Post_CommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post_Comments
    fields = '__all__'

class Post_DetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post_Detail
    fields = '__all__'

