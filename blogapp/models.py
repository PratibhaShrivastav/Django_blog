from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.title

    def publish(self):
        self.publish_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("model_detail", kwargs={"pk": self.pk})
    


class comments(models.Model):
    author=models.CharField(max_length=200)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comments=models.BooleanField(default=False)

    def __str__(self):
        return self.author

    def approve(self):
        self.approved_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    
  
    




