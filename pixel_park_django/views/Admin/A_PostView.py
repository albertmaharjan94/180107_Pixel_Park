from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ...models.Post import Post
from ...models.Comment import Comment
from ...authenticate.authenticate import Auth
from ...models.Photo import Photo

from ...models.User import User
import calendar
import time


@Auth.is_logged_in
@Auth.is_admin
def index(request):
    if request.method == "GET":
        user = User.objects.get(id=request.session['user'])
        posts = Post.objects.all()
        return render(request, 'admin/post/index.html', {'user': user, 'posts': posts})


@Auth.is_logged_in_id
@Auth.is_admin_id
def edit(request, id):
    user = User.objects.get(id=request.session['user']).exclude(is_admin=1)
    p = Post.objects.get(id=id)
    return render(request, 'admin/post/edit.html', {'user': user, 'p': p})


@Auth.is_logged_in
@Auth.is_admin
def create(request):
    u = User.objects.all().exclude(is_admin=1)

    user = User.objects.get(id=request.session['user'])
    return render(request, 'admin/post/create.html', {'user': user, 'u': u})


@Auth.is_logged_in
@Auth.is_admin
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


@Auth.is_logged_in_id
@Auth.is_admin_id
def update(request, id):
    post = Post.objects.get(id=id)

    post.caption = request.POST['caption']
    post.save()

    photo = Photo(post_id=post.id)

    if request.FILES:
        post.photo_set.first().delete(False)
        ext = request.FILES[u'image'].name.split(".")[1].lower()
        file_name = str(calendar.timegm(time.gmtime())) + "." + ext
        photo.photo.save(file_name, request.FILES['image'], save=True)
        photo.save()
        # pass

    return redirect('/admin/posts')


@Auth.is_logged_in_id
@Auth.is_admin_id
def comment(request, id):
    if request.method == "GET":
        user = User.objects.get(id=request.session['user'])
        post = Post.objects.get(id=id)
        return render(request, 'admin/post/comment.html', {'user': user, 'post': post})


@Auth.is_logged_in
@Auth.is_admin
def comment_delete(request):
    c = Comment.objects.get(id=request.POST['id'])
    p = c.post.id
    c.delete()

    return redirect('/admin/posts/comments/' + str(p))


@Auth.is_logged_in_id
@Auth.is_admin_id
def comment_create(request, id):
    user = User.objects.get(id=request.session['user'])
    u = User.objects.all().exclude(is_admin=1)
    p = Post.objects.get(id=id)
    return render(request, 'admin/post/comment-add.html/', {'user': user, 'users': u, 'post': p})


@Auth.is_logged_in_id
@Auth.is_admin_id
def comment_store(request, id):
    u = User.objects.get(id=request.POST['user_id'])

    p = Post.objects.get(id=id)
    Comment(user_id=u.id, post_id=id, title=request.POST['title']).save()

    return redirect('/admin/posts/comments/' + str(p.id))


@Auth.is_logged_in_id
@Auth.is_admin_id
def comment_edit(request, id):
    user = User.objects.get(id=request.session['user'])
    u = User.objects.all().exclude(is_admin=1)
    c = Comment.objects.get(id=id)
    return render(request, 'admin/post/comment-edit.html', {'user': user, 'u': u, 'c': c})


@Auth.is_logged_in_id
@Auth.is_admin_id
def comment_update(request, id):
    c = Comment.objects.get(id=id)
    c.title = request.POST['title']
    c.save()
    return redirect('/admin/posts/comments/' + str(c.post.id))


@Auth.is_logged_in
@Auth.is_admin
def delete(request):
    post = Post.objects.get(id=request.POST['id'])

    post.delete()

    return redirect('/admin/posts')
