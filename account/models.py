from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
    birth = models.DateField()
    image = models.ImageField(upload_to='images/profile')
    created_at = models.DateTimeField(auto_now_add=True)