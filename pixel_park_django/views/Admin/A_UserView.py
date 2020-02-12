from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ...models.User import User
from ...templates.forms import admin_user

import calendar
import time


def index(request):
    if request.method == "GET":
        users = User.objects.all()

        return render(request, 'admin/users/index.html', {'users': users})
    else:
        user = User(
            email=request.POST['email'],
            username=request.POST['username'],
            name=request.POST['name'],
            password=make_password(request.POST['password']),
            image=request.FILES['image'],
        )
        user.save()
        messages.success(request, 'User successfully registered')
        return redirect('/admin/users')


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


def edit(request, id):
    user = User.objects.get(id=id)

    return render(request, 'admin/users/edit.html', {'user': user})


def edit_password(request, id):
    user = User.objects.get(id=id)

    return render(request, 'admin/users/edit-password.html', {'user': user})


def create(request):
    u = admin_user.UserForm(None)
    return render(request, 'admin/users/create.html', {'form': u})


def update(request, id):
    user = User.objects.get(id=id)
    if request.FILES['image']:
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


def update_password(request, id):
    user = User.objects.get(id=id)

    user.password = make_password(request.POST['password'])
    user.save()
    return redirect('/admin/users')
