# Generated by Django 5.0.7 on 2024-07-18 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.AutoField(primary_key=True, serialize=False)),
                ('music_title', models.CharField(max_length=45)),
                ('music_image', models.ImageField(upload_to='')),
                ('music', models.FileField(upload_to='')),
                ('music_detail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32)),
                ('user_image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_title', models.CharField(max_length=45)),
                ('playlist_image', models.ImageField(upload_to='')),
                ('public', models.IntegerField()),
                ('playlist_detail', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'playlist',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistMusic',
            fields=[
                ('music', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.music')),
            ],
            options={
                'db_table': 'playlist_music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicComments',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'music_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicContribute',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
            ],
            options={
                'db_table': 'music_contribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicLiked',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
            ],
            options={
                'db_table': 'music_liked',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('following_user_id', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'user_follow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('followed_user_id', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'db_table': 'user_follower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.user')),
                ('user_email', models.CharField(max_length=45)),
                ('user_password', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_information',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistComments',
            fields=[
                ('playlist', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.playlist')),
                ('comment', models.TextField()),
            ],
            options={
                'db_table': 'playlist_comments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistContribute',
            fields=[
                ('playlist', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.playlist')),
            ],
            options={
                'db_table': 'playlist_contribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlaylistLiked',
            fields=[
                ('playlist', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.playlist')),
            ],
            options={
                'db_table': 'playlist_liked',
                'managed': False,
            },
        ),
    ]
