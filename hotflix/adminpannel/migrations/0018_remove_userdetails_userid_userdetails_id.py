# Generated by Django 4.1.4 on 2022-12-31 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0017_alter_userdetails_userid'),
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
