from django.db import models


# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photo/')
    bio = models.TextField()

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update_profile()


class Image(models.Model):
    image = models.ImageField(upload_to='pic_folder/')
    img_name = models.CharField(max_length=30)
    img_caption = models.TextField()
    img_likes = models.IntegerField(default=0)
    profile = models.ForeignKey(Profile)

    def __str__(self):
        return self.img_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def update_caption(self):
        self.update_caption()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
