from django.db import models

class User(models.Model):
  class Meta:
    managed = False
    db_table = 'user'

  user_id = models.CharField(primary_key=True, max_length=32)
  user_name = models.CharField(max_length=32)
  user_image = models.ImageField()

class UserInformation(models.Model):
  class Meta:
    managed = False
    db_table = 'user_information'

  user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
  user_email = models.CharField(max_length=45)
  user_password = models.CharField(max_length=45)

class UserFollow(models.Model):
  class Meta:
    managed = False
    db_table = 'user_follow'

  user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
  following_user_id = models.CharField(unique=True, max_length=32)

class UserFollower(models.Model):
  class Meta:
    managed = False
    db_table = 'user_follower'
  
  user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
  followed_user_id = models.CharField(unique=True, max_length=32)


class Music(models.Model):
  class Meta:
    managed = False
    db_table = 'music'

  music_id = models.AutoField(primary_key=True)
  user = models.ForeignKey('User', models.DO_NOTHING)
  music_title = models.CharField(max_length=45)
  music_image = models.ImageField()
  music = models.FileField()
  music_detail = models.TextField(blank=True, null=True)

class MusicLiked(models.Model):
  class Meta:
    managed = False
    db_table = 'music_liked'
    unique_together = (('user', 'music'),)

  music = models.ForeignKey(Music, models.DO_NOTHING)
  user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  

class MusicComments(models.Model):
  class Meta:
    managed = False
    db_table = 'music_comments'
    unique_together = (('user', 'music'),)

  music = models.ForeignKey(Music, models.DO_NOTHING)
  user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  
  comment = models.TextField()

class MusicContribute(models.Model):
  class Meta:
    managed = False
    db_table = 'music_contribute'
    unique_together = (('user', 'music'),)

  music = models.ForeignKey(Music, models.DO_NOTHING)
  user = models.OneToOneField('User', models.DO_NOTHING, primary_key=True)  


class Playlist(models.Model):
  class Meta:
    managed = False
    db_table = 'playlist'

  playlist_id = models.AutoField(primary_key=True)
  user = models.OneToOneField('User', models.DO_NOTHING)
  playlist_title = models.CharField(max_length=45)
  playlist_image = models.ImageField()
  public = models.IntegerField()
  playlist_detail = models.TextField(blank=True, null=True)

class PlaylistMusic(models.Model):
  class Meta:
    managed = False
    db_table = 'playlist_music'
    unique_together = (('music', 'playlist'),)

  music = models.OneToOneField(Music, models.DO_NOTHING, primary_key=True) 
  playlist = models.ForeignKey(Playlist, models.DO_NOTHING) 

class PlaylistLiked(models.Model):
  class Meta:
    managed = False
    db_table = 'playlist_liked'
    unique_together = (('playlist', 'user'),)

  playlist = models.OneToOneField(Playlist, models.DO_NOTHING, primary_key=True)  
  user = models.ForeignKey('User', models.DO_NOTHING)

class PlaylistComments(models.Model):
  class Meta:
    managed = False
    db_table = 'playlist_comments'
    unique_together = (('playlist', 'user'),)

  playlist = models.OneToOneField(Playlist, models.DO_NOTHING, primary_key=True)  
  user = models.ForeignKey('User', models.DO_NOTHING)
  comment = models.TextField()

class PlaylistContribute(models.Model):
  class Meta:
    managed = False
    db_table = 'playlist_contribute'
    unique_together = (('playlist', 'user'),)

  playlist = models.OneToOneField(Playlist, models.DO_NOTHING, primary_key=True)  
  user = models.ForeignKey('User', models.DO_NOTHING)

