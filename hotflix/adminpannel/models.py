from django.db import models
from django.contrib.auth.models import User


# create a tuple for the status of each post

class UserDetails(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    email = models.EmailField(max_length=100 , unique=True)
    password = models.CharField(max_length=100)


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
    
	

# each field in this class represents a column in the database table






# # Create your models here.
# class imageupload(models.Model):

# 	# file will be uploaded to MEDIA_ROOT / uploads
# 	upload = models.ImageField(upload_to ='uploads/')
# 	videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")



# class Card(models.Model):
#     class Suit(models.IntegerChoices):
#         DIAMOND = 1
#         SPADE = 2
#         HEART = 3
#         CLUB = 4

#     suit = models.IntegerField(choices=Suit.choices)
#     upload = models.ImageField(upload_to ='uploads/')
#     videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
	

# 	# or...
# 	# file will be saved to MEDIA_ROOT / uploads / 2015 / 01 / 30
# 	# upload = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
