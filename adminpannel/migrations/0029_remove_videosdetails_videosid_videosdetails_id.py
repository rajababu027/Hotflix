# Generated by Django 4.1.4 on 2023-01-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0028_remove_videosdetails_id_videosdetails_videosid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videosdetails',
            name='videosId',
        ),
        migrations.AddField(
            model_name='videosdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, default=2, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]