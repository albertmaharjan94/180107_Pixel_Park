from datetime import datetime

from django.db import models
from ..models.User import User


# Create your models here.
class Follow(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'follows'
