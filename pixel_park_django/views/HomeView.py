import os

from django.contrib.messages.storage import session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from ..authenticate.authenticate import Auth
from django.template.loader import render_to_string
from django.core import serializers
from django.db.models import Q
from ..models.User import User
from ..models.Post import Post
from ..models.Like import Like
from ..models.Comment import Comment
from ..models.Follow import Follow
from django.http import HttpResponseRedirect


def search(request):
    search = request.GET['search']

    user = User.objects.filter(Q(name__icontains=search) | Q(username__icontains=search) | Q(email__icontains=search))
    html = render_to_string('users/home/render/search.html', {'users': user, 'search': search})
    return JsonResponse({'data': html})


@Auth.is_logged_in
def index(request):
    # return HttpResponse(request.session['user'])
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        request.session.flush()
        return redirect('/login')
    try:
        follow = Follow.objects.filter(follower_id=request.session['user']).values_list('following_id', flat=True)
    except:
        follow = []
    try:
        post = Post.objects.filter(Q(user_id__in=follow) | Q(user_id=request.session['user'])).order_by('-date')
        # post = User.objects.get(id=2).post_set.all()
    except:
        request.session.flush()
        return redirect('/login')

    # test

    # test end
    following_list = user.follower.all().values_list('following_id', flat=True)
    suggestion = User.objects.exclude(Q(id__in=following_list) | Q(id=user.id))

    return render(request, 'users/home/index.html', {'user': user, 'posts': post, 'suggestions': suggestion})


@Auth.is_logged_in
def logout(request):
    request.session.flush()
    return redirect('/login')


@Auth.is_logged_in
def follow_profile(request):
    follow = Follow.objects.filter(Q(follower_id=request.session['user']) & Q(following_id=request.POST['profile_id']))
    try:
        follower = User.objects.get(id=request.session['user'])
        following = User.objects.get(id=request.POST['profile_id'])
    except:
        return redirect('/index')
    if not follow:
        Follow(follower=follower, following=following).save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@Auth.is_logged_in
def unfollow_profile(request):
    follow = Follow.objects.filter(Q(follower_id=request.session['user']) & Q(following_id=request.POST['profile_id']))
    try:
        follower = User.objects.get(id=request.session['user'])
        following = User.objects.get(id=request.POST['profile_id'])
    except:
        return redirect('/index')
    if follow:
        follow.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@Auth.is_logged_in_id
def profile(request, id):
    try:
        profile = User.objects.get(id=id)
        user = User.objects.get(id=request.session['user'])

    except:
        request.session.flush()
        return redirect('/login')
    follow_count = Follow.objects.filter(follower_id=profile.id).count()
    follower_count = Follow.objects.filter(following_id=profile.id).count()

    follower_list = user.follower.filter(follower_id=user.id).values_list('following_id', flat=True)
    return render(request, 'users/home/profile.html',
                  {'user': user, 'profile': profile, 'following_count': follow_count, 'follower_count': follower_count,
                   'follower_list': follower_list})


@Auth.is_logged_in_id
def profile_photo(request, id):
    try:
        user = User.objects.get(id=request.session['user'])
        post = Post.objects.filter(id=id)
    except:
        request.session.flush()
        return redirect('/login')

    html = render_to_string('users/home/render/post.html', {'post': post.first(), 'user': user})
    return JsonResponse({'html': html})


# follower list
def follower_list(request, id):
    try:
        user = User.objects.get(id=request.session['user'])
        profile = User.objects.get(id=id)

    except:
        return redirect('/profile/' + id)

    follow = Follow.objects.filter(following_id=profile.id)
    follower_list = user.follower.filter(follower_id=user.id).values_list('following_id', flat=True)
    html = render_to_string('users/home/render/follower.html',
                            {'follow': follow, 'user': user, 'follower_list': follower_list},request=request)
    return JsonResponse({'html': html})


# following list
def following_list(request, id):
    try:
        user = User.objects.get(id=request.session['user'])
        profile = User.objects.get(id=id)

    except:
        return redirect('/profile/' + id)

    following = Follow.objects.filter(follower_id=profile.id)
    following_list = user.follower.filter(follower_id=user.id).values_list('following_id', flat=True)
    html = render_to_string('users/home/render/following.html',
                            {'following': following, 'user': user, 'following_list': following_list},request=request)
    return JsonResponse({'html': html})


# like list
def like_list(request, id):
    try:
        user = User.objects.get(id=request.session['user'])
        post = Post.objects.get(id=id)

    except:
        return JsonResponse({'html': ''})

    likes = post.like_set.all();
    following_list = user.follower.filter(follower_id=user.id).values_list('following_id', flat=True)
    html = render_to_string('users/home/render/like.html',
                            {'likes': likes, 'user': user, 'following_list': following_list}, request=request)
    return JsonResponse({'html': html})


# get notification ajax
def get_notification(request):
    user = User.objects.filter(id=request.session['user'])

    notificationList = list()
    for p in user.first().post_set.all():
        for l in p.like_set.all():
            if l.user_id != request.session['user']:
                notificationList.append(
                    {'type': 'like', 'user_id': l.user.id, 'user_name': l.user.username, 'user_image': l.user.image,
                     'post_id': p.id, 'post_image': p.photo_set.first().photo,
                     'date': l.date})
        for c in p.comment_set.all():
            if c.user_id != request.session['user']:
                notificationList.append(
                    {'type': 'comment', 'user_id': c.user.id, 'user_name': c.user.username, 'user_image': c.user.image,
                     'post_id': p.id, 'post_image': p.photo_set.first().photo,
                     'date': c.date})
    for f in user.first().following.all():
        notificationList.append(
            {'type': 'follow', 'user_id': f.follower.id, 'user_name': f.follower.username, 'image': f.follower.image,
             'date': f.date})
    sortedNotification = sorted(notificationList, key=lambda i: i['date'], reverse=True)

    html = render_to_string('users/home/render/notification.html',
                            {'notifications': sortedNotification, 'user': user.first()})
    return JsonResponse({'html': html})


@Auth.is_logged_in_id
def profile_image_update(request, id):
    if id != request.session['user']:
        request.session.flush()
        return redirect('/login')
    else:
        try:
            user = User.objects.get(id=id)
        except:
            request.session.flush()
            return redirect('/login')
        if user.image != 'user.png':
            user.image.delete(False)

        user.image = request.FILES['image']
        user.save()
        return redirect('/profile/' + str(user.id))


# post like
def profile_like(request, post_id, user_id):
    like = Like.objects.filter(user_id=user_id, post_id=post_id)
    stat = False
    # return JsonResponse({'data':like.count()})
    if not like:
        Like(user_id=user_id, post_id=post_id).save()
        stat = True

    return JsonResponse({'data': stat})


# post unlike
def profile_unlike(request, post_id, user_id):
    like = Like.objects.filter(user_id=user_id, post_id=post_id)
    stat = False
    # return JsonResponse({'data':like.count()})
    if like:
        like.delete()
        stat = True

    return JsonResponse({'data': stat})


# commenton post
def comment(request):
    try:
        comment = Comment(user_id=request.POST['user_id'], post_id=request.POST['post_id'],
                          title=request.POST['comment']).save()
    except:
        return JsonResponse({'data': {'success': False}})
    return JsonResponse({'data': {'success': True, 'comment': comment}})