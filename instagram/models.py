from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_image = models.ImageField(upload_to='profile_photo/', blank=True, default='profile_photo/sea_side.jpeg')
    bio = models.CharField(max_length=50, blank=True)

    def save_profile(self):
        self.save()

    def __str__(self):
        return f'{self.user.username} Profile'

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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def save_image(self):
        self.save()

    def __str__(self):
        return f'{self.profile.user.username}'

    @classmethod
    def get_image(request, id):
        try:
            image = Image.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return image

    class Meta:
        ordering = ['-post_date']

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
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default='pic_folder/eat_us.jpg')

    def __str__(self):
        return f'{self.username}'

    class Meta:
        ordering = ['-date']

    @classmethod
    def get_all_comments(cls):
        comments = Comment.objects.all()
        return comments
