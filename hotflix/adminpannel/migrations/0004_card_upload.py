# Generated by Django 4.1.4 on 2022-12-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpannel', '0003_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='upload',
            field=models.ImageField(default=2, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
