# Generated by Django 4.1.4 on 2022-12-31 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0015_alter_userdetails_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='userId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]