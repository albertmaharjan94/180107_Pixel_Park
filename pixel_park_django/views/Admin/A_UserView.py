from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ...models.User import User
from ...templates.forms import admin_user
from ...authenticate.authenticate import Auth
import calendar
import time


@Auth.is_logged_in
@Auth.is_admin
def index(request):
    if request.method == "GET":
        users = User.objects.filter(is_admin=0)

        user = User.objects.get(id=request.session['user'])
        return render(request, 'admin/users/index.html', {'user':user,'users': users})
    else:
        user = User(
            email=request.POST['email'],
            username=request.POST['username'],
            name=request.POST['name'],
            password=make_password(request.POST['password']),
            image= request.FILES['image'] if request.FILES else 'user.png',
        )
        user.save()
        messages.success(request, 'User successfully registered')
        return redirect('/admin/users')


@Auth.is_logged_in
@Auth.is_admin
def delete(request):

    users = User.objects.get(id=request.POST['id'])
    if users.image != 'user.png':
        users.image.delete(False)
    users.delete()
    # try:
    #
    # except:
    #     return redirect('/admin/users')

    return redirect('/admin/users')


@Auth.is_logged_in_id
@Auth.is_admin_id
def edit(request, id):

    user=User.objects.get(id=request.session['user'])
    users = User.objects.get(id=id)

    return render(request, 'admin/users/edit.html', {'user':user,'users': users})


@Auth.is_logged_in_id
@Auth.is_admin_id
def edit_password(request, id):
    users = User.objects.get(id=id)

    user=User.objects.get(id=request.session['user'])
    return render(request, 'admin/users/edit-password.html', {'user': user,'users':users})


@Auth.is_logged_in
@Auth.is_admin
def create(request):

    user=User.objects.get(id=request.session['user'])
    u = admin_user.UserForm(None)
    return render(request, 'admin/users/create.html', {'user':user,'form': u})


@Auth.is_logged_in_id
@Auth.is_admin_id
def update(request, id):
    user = User.objects.get(id=id)
    if request.FILES:
        if user.image != 'user.png':
            user.image.delete(False)

        ext = request.FILES[u'image'].name.split(".")[1].lower()
        file_name = str(calendar.timegm(time.gmtime())) + "." + ext
        user.image.save(file_name, request.FILES['image'], save=True)
    user.name = request.POST['name']
    user.email = request.POST['email']
    user.username = request.POST['username']

    user.save()

    return redirect('/admin/users')


@Auth.is_logged_in_id
@Auth.is_admin_id
def update_password(request, id):
    user = User.objects.get(id=id)

    user.password = make_password(request.POST['password'])
    user.save()
    return redirect('/admin/users')
