from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow(models.Model):
    send = models.ForeignKey(User, related_name='send', on_delete='CASCADE') # 팔로우 한 사람
    receive = models.ForeignKey(User, related_name='receive', on_delete='CASCADE') # 팔로우 받은 사람
    created_at = models.DateTimeField(auto_now_add=True)
