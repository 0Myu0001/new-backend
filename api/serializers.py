from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class UserInformationSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserInformation
    fields = '__all__'

class UserFollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserFollow
    fields = '__all__'

class UserFollowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserFollower
    fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
  class Meta:
    model = Music
    fields = '__all__'

class MusicLikedSerializer(serializers.ModelSerializer):
  class Meta:
    model = MusicLiked
    fields = '__all__'

class MusicCommentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = MusicComments
    fields = '__all__'

class MusicContributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = MusicContribute
    fields = '__all__'

class PlaylistSerializer(serializers.ModelSerializer):
  class Meta:
    model = Playlist
    fields = '__all__'

class PlaylistMusicSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlaylistMusic
    fields = '__all__'

class PlaylistLikedSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlaylistLiked
    fields = '__all__'

class PlaylistContributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PlaylistContribute
    fields = '__all__'

# class PlaylistCommentsSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = PlaylistComments
#     fields = '__all__'
