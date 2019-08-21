from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='images/post', null=True)
    user = models.ForeignKey(User, on_delete='CASCADE')
    category = models.CharField(max_length=200, default='animal')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)