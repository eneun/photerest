from django.db import models
from django.contrib.auth.models import User
from post.models import Post

# Create your models here.
class Comment(models.Model):
    content = models.TextField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)