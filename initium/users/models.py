from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    phoneNumber = models.CharField(max_length=30, default='1')
    classification = models.CharField(max_length=50, default='Other')
    country = models.CharField(max_length=50, default='Kazakhstan')
    city = models.CharField(max_length=50, default='Almaty')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            outsize = (300, 300)
            img.thumbnail(outsize)
            img.save(self.image.path)
