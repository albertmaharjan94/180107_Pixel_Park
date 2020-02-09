from django.db import models


# Create your models here.
class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=240)
    password = models.CharField(max_length=191)
    social_link = models.TextField(default='')
    is_admin = models.IntegerField(default=0)
    image = models.ImageField(default='user.png')

    class Meta:
        db_table = 'users'
