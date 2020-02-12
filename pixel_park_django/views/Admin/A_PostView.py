from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ...models.Post import Post
from ...models.Comment import Comment

from ...models.Photo import Photo

from ...models.User import User
import calendar
import time


def index(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'admin/post/index.html', {'posts': posts})


def edit(request, id):
    p = Post.objects.get(id=id)
    return render(request, 'admin/post/edit.html', {'p': p})


def create(request):
    u = User.objects.all()

    return render(request, 'admin/post/create.html', {'u': u})


def store(request):
    if not request.FILES['image']:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    post = Post(user_id=request.POST['user_id'], caption=request.POST['caption'])
    post.save()
    ext = request.FILES[u'image'].name.split(".")[1].lower()
    file_name = str(calendar.timegm(time.gmtime())) + "." + ext
    photo = Photo(post_id=post.id, photo=file_name)
    photo.save()
    photo.photo.save(file_name, request.FILES['image'], save=True)
    return redirect('/admin/posts')


def update(request, id):
    post = Post.objects.get(id=id)

    if request.FILES['image']:
        post.photo_set.first().delete(False)
        # pass
    post.caption = request.POST['caption']
    post.save()

    photo = Photo(post_id=post.id)

    ext = request.FILES[u'image'].name.split(".")[1].lower()
    file_name = str(calendar.timegm(time.gmtime())) + "." + ext
    photo.photo.save(file_name, request.FILES['image'], save=True)
    photo.save()

    return redirect('/admin/posts')


def comment(request, id):
    if request.method == "GET":
        post = Post.objects.get(id=id)
        return render(request, 'admin/post/comment.html', {'post': post})


def comment_delete(request):
    c = Comment.objects.get(id=request.POST['id'])
    p = c.post.id
    c.delete()

    return redirect('/admin/posts/comments/' + str(p))


def comment_create(request, id):
    u = User.objects.all()
    p = Post.objects.get(id=id)
    return render(request, 'admin/post/comment-add.html/', {'users': u, 'post': p})


def comment_store(request, id):
    u = User.objects.get(id=request.POST['user_id'])

    p = Post.objects.get(id=id)
    Comment(user_id=u.id, post_id=id, title=request.POST['title']).save()

    return redirect('/admin/posts/comments/' + str(p.id))


def comment_edit(request, id):
    c = Comment.objects.get(id=id)
    return render(request, 'admin/post/comment-edit.html', {'c': c})


def comment_update(request, id):
    c = Comment.objects.get(id=id)
    c.title = request.POST['title']
    c.save()
    return redirect('/admin/posts/comments/' + str(c.post.id))


def delete(request):
    post = Post.objects.get(id=request.POST['id'])

    post.delete()

    return redirect('/admin/posts')
