from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ...models.User import User
from ...models.Post import Post


def index(request):
    userCount=len(User.objects.all())

    postCount=len(Post.objects.all())
    return render(request, 'admin/dashboard.html',{'uc':userCount,'pc':postCount})
