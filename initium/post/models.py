from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    CATEGORY_CHOICES = (
        ('it', 'IT'),
        ('sport', 'Sport'),
        ('health', 'Health'),
        ('electronic', 'Electronic'),
        ('transport', 'Transport'),
        ('culture', 'Culture'),
        ('other', 'Other'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')

    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
    pledgeAmount = models.IntegerField(default=0)
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES, default='other')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Donation(models.Model):
    donator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='+')
    done = models.DateTimeField(auto_now_add=True)
    sum = models.IntegerField(default=0)

class ChatHistory(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
