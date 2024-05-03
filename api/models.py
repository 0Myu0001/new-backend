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

