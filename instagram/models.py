from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photo/')
    bio = models.TextField()

    def __str__(self):
        return self.bio


class Image(models.Model):
    image = models.ImageField(upload_to='pic_folder/')
    img_name = models.CharField(max_length=30)
    img_caption = models.TextField()
    img_likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.img_name
