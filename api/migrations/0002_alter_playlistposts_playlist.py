# Generated by Django 5.0.4 on 2024-06-15 05:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistposts',
            name='playlist',
            field=models.ForeignKey(db_column='playlist_id', on_delete=django.db.models.deletion.CASCADE, to='api.playlist', to_field='playlist_id'),
        ),
    ]
