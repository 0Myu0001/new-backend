# Generated by Django 5.0.4 on 2024-05-18 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_playlist_comments_playlist_loved_post_loved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/', verbose_name='user_image'),
        ),
    ]
