from django.db import models

# Create your models here.
class User (models.Model):
  class meta:
    db_table = 'user'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  user_name = models.CharField(
      verbose_name='user_name',
      blank=True,
      null=True,
      max_length=30,
      default='',
  )

  user_email = models.CharField(
      verbose_name='user_email',
      blank=True,
      null=True,
      max_length=254,
      default='',
  )

  def __str__(self):
      return self.user_id
  
class User_Strict_Information (models.Model):
  class meta:
    db_table = 'user_strict_information'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  user_email = models.CharField(
      verbose_name='user_email',
      blank=True,
      null=True,
      max_length=254,
      default='',
  )

  user_real_name = models.CharField(
      verbose_name='user_real_name',
      blank=True,
      null=True,
      max_length=30,
      default='',
  )

  user_phone_number = models.CharField(
      verbose_name='user_phone_number',
      blank=True,
      null=True,
      max_length=30,
      default='',
  )

  user_age = models.IntegerField(
      verbose_name='user_age',
      blank=True,
      null=True,
      default=0,
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
  
class User_Experience (models.Model):
  class meta:
    db_table = 'user_experience'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  recent = models.CharField(
    verbose_name='user_experience_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  liked = models.CharField(
      verbose_name='user_experience_title',
      blank=True,
      null=True,
      max_length=30,
      default='',
  )

  def __str__(self):
      return self.user_experience_id
  
class Playlist (models.Model):
  class meta:
    db_table = 'playlist'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  playlist_id = models.CharField(
    verbose_name='playlist_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  playlist_name = models.CharField(
      verbose_name='playlist_name',
      blank=True,
      null=True,
      max_length=30,
      default='',
  )

  def __str__(self):
      return self.play_list_id
  
class Notification (models.Model):
  class meta:
    db_table = 'notification'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

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

class Post (models.Model):
  class meta:
    db_table = 'post'

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  post_id = models.CharField(
    verbose_name='post_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
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

  post_content = models.CharField(
      verbose_name='post_content',
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

  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  post_id = models.CharField(
    verbose_name='post_id',
    blank=True,
    null=True,
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
  
class Post_Detail (models.Model):
  class meta:
    db_table = 'post_detail'

  post_id = models.CharField(
    verbose_name='post_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  post_detail_id = models.CharField(
    verbose_name='post_detail_id',
    blank=True,
    null=True,
    max_length=30,
    default='',
  )

  post_detail_content = models.CharField(
      verbose_name='post_detail_content',
      blank=True,
      null=True,
      max_length=1000,
      default='',
  )

  def __str__(self):
      return self.post_detail_id

