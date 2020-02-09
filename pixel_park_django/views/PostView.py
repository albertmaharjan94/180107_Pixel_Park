from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..authenticate.authenticate import Auth
from ..models import Post, Photo

import base64
from django.core.files.base import ContentFile
import datetime
import calendar
import time
import urllib


# ts =

def upload(request):
    image_data = request.POST['photo']
    format, imgstr = image_data.split(';base64,')
    ext = format.split('/')[-1]

    data = ContentFile(base64.b64decode(imgstr))
    file_name = str(calendar.timegm(time.gmtime())) + "." + ext
    post = Post.Post(user_id=request.session['user'], caption=request.POST['caption'])
    post.save()
    photo = Photo.Photo(post_id=post.id, photo=file_name)
    photo.save()
    photo.photo.save(file_name, data, save=True)
    return redirect('/index')
