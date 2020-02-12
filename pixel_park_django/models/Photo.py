import os
import urllib

from django.core.files import File
from django.db import models
from django.db.models.signals import post_delete

from ..models.Post import Post
from django.dispatch import receiver


# Create your models here.
class Photo(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(default='image.img')
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'photos'

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                os.path.basename(self.url),
                File(open(result[0], 'rb'))
            )
            self.save()


@receiver(post_delete, sender=Photo)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
