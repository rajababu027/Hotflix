# Generated by Django 4.1.4 on 2023-01-04 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0024_alter_videosdetails_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videosdetails',
            name='genre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='videosdetails',
            name='type',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
