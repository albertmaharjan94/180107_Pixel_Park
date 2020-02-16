from django.contrib.messages.storage import session
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from ..authenticate.authenticate import Auth
from django.http import JsonResponse
from pixel_park_django.models.User import User
from django.core.validators import validate_email
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

from ..templates.forms import users


@Auth.is_guest
def home(request):
    return redirect('/login')


@Auth.is_guest
def login(request):
    if request.method == 'GET':
        return render(request, 'users/auth/login.html', {'f': users.LoginForm})


@Auth.is_guest
def register(request):
    return render(request, 'users/auth/register.html')


@Auth.is_guest
def forget(request):
    return render(request, 'users/auth/forget.html')


@Auth.is_guest
def store(request):
    try:
        validate_email(request.POST['email'])
    except:
        messages.error(request, 'Email not valid')
        return redirect('/register')

    user = User(
        email=request.POST['email'],
        username=request.POST['username'],
        name=request.POST['name'],
        password=make_password(request.POST['password'])
    )
    user.save()
    messages.success(request, 'User successfully registered')
    return redirect('/login')


# Check for email

def hasEmail(request):
    email = request.POST['email']
    data = User.objects.filter(email=email).exists()
    return JsonResponse({'data': {'status': data}}, safe=False)


# Check for username

def hasUsername(request):
    username = request.POST['username']
    data = User.objects.filter(username=username).exists()
    return JsonResponse({'data': {'status': data}}, safe=False)


# @Auth.is_guest
# def index(request):
#     return HttpResponse("Index Page")
# @Auth.is_guest
def logged(request):
    try:
        user = User.objects.get(email=request.POST['email'])
    except:
        messages.error(request, 'Email not found. Please try again.')
        return redirect('/login')

    if not check_password(request.POST['password'], str(user.password)):
        messages.error(request, 'Password did not match. Please try again.')
        return redirect('/login')
    else:
        request.session['user'] = user.id
        if user.is_admin == 0:
            return redirect('/index')
        else:
            return redirect('/admin')


@Auth.is_logged_in_id
@Auth.is_user_id
def edit_user(request, id):
    if request.session['user'] != id:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        request.session.flush()
        return redirect('/login')

    return render(request, 'users/home/profile-edit.html', {'user': user})


@Auth.is_logged_in_id
@Auth.is_user_id
def edit_password(request, id):
    if request.session['user'] != id:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        request.session.flush()
        return redirect('/login')

    return render(request, 'users/home/profile-password.html', {'user': user})


@Auth.is_logged_in_id
@Auth.is_user_id
def update_password(request, id):
    if request.session['user'] != id:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        request.session.flush()
        return redirect('/login')

    if not check_password(request.POST['old_pass'], str(user.password)):
        messages.error(request, "The password did not match with your old one")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    if request.POST['new_pass'] != request.POST['confirm_pass']:
        messages.error(request, "New password and confirmation did not match. Please try again")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    user.password = make_password(request.POST['new_pass'])
    user.save()
    return redirect('/profile/' + str(user.id))


@Auth.is_logged_in_id
@Auth.is_user_id
def update_user(request, id):
    # return HttpResponse(request.POST)
    if request.session['user'] != id:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    try:
        user = User.objects.get(id=request.session['user'])
    except:
        request.session.flush()
        return redirect('/login')

    user.name = request.POST['name']
    user.email = request.POST['email']
    user.username = request.POST['username']
    user.social_link = request.POST['social_link']
    user.save()

    return redirect('/profile/' + str(user.id))
