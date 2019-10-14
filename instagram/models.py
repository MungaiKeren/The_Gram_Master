from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='profile_photo/', blank=True)
    bio = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update_profile()


class Image(models.Model):
    image = models.ImageField(upload_to='pic_folder/')
    img_name = models.CharField(max_length=30)
    img_caption = models.CharField(max_length=40, blank=True)
    img_likes = models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile.user.username}'

    class Meta:
        ordering = ['-post_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def update_caption(self, caption):
        self.img_caption = caption
        self.save()

    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images


class Comment(models.Model):
    total_comments = models.IntegerField(default=0)
    username = models.CharField(blank=True, max_length=50)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}'
