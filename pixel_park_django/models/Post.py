from datetime import datetime

from django.db import models
from ..models.User import User


# Create your models here.
class Post(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        db_table = 'posts'
