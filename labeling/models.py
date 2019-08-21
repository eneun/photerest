from django.db import models
from post.models import Post

# Create your models here.
class Label(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    post = models.ForeignKey(Post, related_name='category_set', on_delete=models.CASCADE)
    category = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)