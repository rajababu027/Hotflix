# Generated by Django 4.1.4 on 2023-01-04 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0022_remove_videosdetails_videos_videosdetails_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosdetails',
            name='id',
        ),
        migrations.AddField(
            model_name='videosdetails',
            name='videosId',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
