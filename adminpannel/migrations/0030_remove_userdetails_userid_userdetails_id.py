# Generated by Django 4.1.5 on 2023-01-15 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0029_remove_videosdetails_videosid_videosdetails_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='userId',
        ),
        migrations.AddField(
            model_name='userdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
