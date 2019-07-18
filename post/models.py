from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=1500)
    image = models.ImageField(upload)