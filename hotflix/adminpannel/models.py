from django.db import models
from django.contrib.auth.models import User 



# create a tuple for the status of each post

class UserDetails(models.Model):
    userId = models.IntegerField(default=0 ,primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100 , unique=True)
    password = models.CharField(max_length=100)
    def save(self, *args, **kwargs):
        userid = UserDetails.objects.all()

        if userid.exists() and self._state.adding:
            last_userid = userid.latest('userId')
            self.userId = int(last_userid.userId) + 1
        super().save(*args, **kwargs)


class VideosDetails(models.Model):
    class VIDEOS(models.TextChoices):
        MusicVideos = 'Music Videos'
        WebSeries = 'Web Series'
        Movies = 'Movies'
        Trailers = 'Trailers'
        Kids = 'Kids'
        Devotional = 'Devotional'


    image = models.ImageField(upload_to ='image/')
    titleImage = models.ImageField(upload_to ='titleImage/')
    thumbnailImage = models.ImageField(upload_to ='thumbnailImage/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    year = models.IntegerField()
    genre = models.CharField(max_length=100)
    Duration = models.CharField(max_length=100)
    VIDEOS = models.CharField(
        max_length=12,
        choices=VIDEOS.choices,
        default=VIDEOS.MusicVideos,
    )
    trailer = models.FileField(upload_to='tailers/', null=True, verbose_name="Trailer")
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video")
    
