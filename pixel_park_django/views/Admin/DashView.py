from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from ...models.User import User
from ...models.Post import Post
from ...authenticate.authenticate import Auth


@Auth.is_logged_in
@Auth.is_admin
def index(request):
    user = User.objects.get(id=request.session['user'])
    userCount = len(User.objects.all())

    postCount = len(Post.objects.all())
    return render(request, 'admin/dashboard.html', {'user': user, 'uc': userCount, 'pc': postCount})
