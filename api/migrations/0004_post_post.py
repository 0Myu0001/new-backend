# Generated by Django 5.0.4 on 2024-05-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_notification_playlist_post_comments_post_detail_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post',
            field=models.FileField(blank=True, null=True, upload_to='posts/', verbose_name='post'),
        ),
    ]
