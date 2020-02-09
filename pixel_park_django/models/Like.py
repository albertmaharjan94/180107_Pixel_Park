from datetime import datetime

from django.db import models
from ..models import Post, User


# Create your models here.
class Like(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    post = models.ForeignKey(Post.Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User.User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'likes'
