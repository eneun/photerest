from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='images/post')

    def summary(self):
        return self.content[:20]
        
    def __str__(self):
        return self.summary