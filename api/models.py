from django.db import models

# Create your models here.
class User (models.Model):
  class meta:
    db_table = 'user'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    primary_key=True, 
    max_length=25,
    default='',
    unique=True, 
  )

  user_name = models.CharField(
    verbose_name='user_name',
    blank=True,
    null=True,
    max_length=25,
    default='',
  )

  user_email = models.CharField(
    verbose_name='user_email',
    blank=True,
    null=True,
    max_length=254,
    default='',
  )

  user_image = models.ImageField(
    verbose_name='user_image',
    blank=True,
    null=True,
    upload_to='user_images/',
  )

  follower_number = models.IntegerField(
    verbose_name='follower_number',
    blank=True,
    null=True,
    default=0,
  )

  following_number = models.IntegerField(
    verbose_name='following_number',
    blank=True,
    null=True,
    default=0,
  )
  
  listened_number = models.IntegerField(
    verbose_name='listened_number',
    blank=True,
    null=True,
    default=0,
  )

  def __str__(self):
    return self.user_id
  
class User_Followers(models.Model):
  class Meta:
    db_table = 'user_followers'
  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  follower_id = models.CharField(
    verbose_name='follower_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  def __str__(self):
    return self.user_id
  
class User_Followings(models.Model):
  class Meta:
    db_table = 'user_followings'
    user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  following_id = models.CharField(
    verbose_name='following_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  def __str__(self):
    return self.user_id


class User_Strict_Information (models.Model):
  class meta:
    db_table = 'user_strict_information'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  user_email = models.CharField(
    verbose_name='user_email',
    blank=True,
    null=True,
    max_length=254,
    default='',
  )

  user_phone_number = models.CharField(
    verbose_name='user_phone_number',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  user_birth = models.DateField(
    verbose_name='user_birth',
    blank=True,
    null=True,
  )

  user_password = models.CharField(
    verbose_name='user_password',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  def __str__(self):
    return self.user_id


class Post (models.Model):
  class meta:
    db_table = 'post'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  post_id = models.CharField(
    verbose_name='post_id',
    blank=True,
    primary_key=True, 
    max_length=30,
    default='',
    unique=True, 
  )

  post = models.FileField(
    verbose_name='post',
    blank=True,
    null=True,
    upload_to='posts/',
  )

  post_title = models.CharField(
    verbose_name='post_title',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  post_image = models.ImageField(
    verbose_name='post_image',
    blank=True,
    null=True,
    upload_to='images/',
  )

  post_played_times = models.IntegerField(
    verbose_name='post_played_times',
    blank=True,
    null=True,
    default=0,
  )

  post_loved_number = models.IntegerField(
    verbose_name='post_loved_number',
    blank=True,
    null=True,
    default=0,
  )

  post_comment_number = models.IntegerField(
    verbose_name='post_comment_number',
    blank=True,
    null=True,
    default=0,
  )

  post_saved_number = models.IntegerField(
    verbose_name='post_saved_number',
    blank=True,
    null=True,
    default=0,
  )

  post_detail = models.CharField(
    verbose_name='post_detail',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  post_tags = models.CharField(
    verbose_name='post_tags',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  def __str__(self):
    return self.post_id


class Post_Comments (models.Model):
  class meta:
    db_table = 'post_comments'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  post_id = models.CharField(
    verbose_name='post_id',
    blank=True,
    primary_key=True, 
    max_length=30,
    default='',
  )

  comment_id = models.CharField(
    verbose_name='comment_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  comment_content = models.CharField(
    verbose_name='comment_content',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  def __str__(self):
      return self.comment_id
  
class Post_Loved (models.Model):
  class meta:
    db_table = 'post_loved'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  post_id = models.ForeignKey(Post, to_field='post_id', db_column='post_id', on_delete=models.CASCADE)

  loved_by_user_id = models.CharField(
    verbose_name='loved_by_user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  def __str__(self):
    return self.post_id


class Playlist (models.Model):
  class meta:
    db_table = 'playlist'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  playlist_id = models.CharField(
    verbose_name='playlist_id',
    blank=True,
    primary_key=True, 
    max_length=30,
    default='',
    unique=True, 
  )

  playlist_title = models.CharField(
    verbose_name='playlist_name',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  playlist_image = models.ImageField(
    verbose_name='playlist_image',
    blank=True,
    null=True,
    upload_to='playlist_images/',
  )

  posts = models.ManyToManyField(Post, through='PlaylistPosts')

  public = models.BooleanField(
    verbose_name='public',
    default=True,
  )

  playlist_played_times = models.IntegerField(
    verbose_name='playlist_played_times',
    blank=True,
    null=True,
    default=0,
  )

  playlist_loved_number = models.IntegerField(
    verbose_name='playlist_loved_number',
    blank=True,
    null=True,
    default=0,
  )

  playlist_comment_number = models.IntegerField(
    verbose_name='playlist_comment_number',
    blank=True,
    null=True,
    default=0,
  )

  playlist_saved_number = models.IntegerField(
    verbose_name='playlist_saved_number',
    blank=True,
    null=True,
    default=0,
  )

  playlist_detail = models.CharField(
    verbose_name='playlist_detail',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  playlist_attributes = models.CharField(
    verbose_name='playlist_attributes',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  def __str__(self):
    return self.playlist_id
  
class PlaylistPosts (models.Model):
  playlist = models.ForeignKey(Playlist, to_field='playlist_id', db_column='playlist_id', on_delete=models.CASCADE)
  post = models.ForeignKey(Post, to_field='post_id', db_column='post_id', on_delete=models.CASCADE)

class Playlist_Comments (models.Model):
  class meta:
    db_table = 'playlist_comments'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  playlist_id = models.ForeignKey(Playlist, to_field='playlist_id', db_column='playlist_id', on_delete=models.CASCADE)

  comment_id = models.CharField(
    verbose_name='comment_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  comment_content = models.CharField(
    verbose_name='comment_content',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  def __str__(self):
    return self.comment_id

class Playlist_Loved (models.Model):
  class meta:
    db_table = 'playlist_loved'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  playlist_id = models.ForeignKey(Playlist, to_field='playlist_id', db_column='playlist_id', on_delete=models.CASCADE)

  loved_by_user_id = models.CharField(
    verbose_name='loved_by_user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  def __str__(self):
    return self.playlist_id  


class Notification (models.Model):
  class meta:
    db_table = 'notification'

  user_id = models.ForeignKey(User, to_field='user_id', db_column='user_id', on_delete=models.CASCADE)

  notification_id = models.CharField(
    verbose_name='notification_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  notification_content = models.CharField(
    verbose_name='notification_content',
    blank=True,
    null=True,
    max_length=1000,
    default='',
  )

  def __str__(self):
    return self.notification_id
