# Generated by Django 4.1.4 on 2023-01-03 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0020_alter_userdetails_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosdetails',
            name='Duration',
        ),
    ]
