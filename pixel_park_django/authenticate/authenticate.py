from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from ..models.User import User


class Auth:
    def is_logged_in(function):
        def wrap(request):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user'])) != 0:
                    return function(request)
                else:
                    request.session.flush()
                    return redirect('/login')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap

    def is_admin(function):
        def wrap(request):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user']).filter(is_admin=1)) != 0:
                    return function(request)
                else:
                    return redirect('/index')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap

    def is_admin_id(function):
        def wrap(request,id):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user']).filter(is_admin=1)) != 0:
                    return function(request,id)
                else:
                    return redirect('/index')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap

    def is_user(function):
        def wrap(request):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user']).filter(is_admin=0)) != 0:
                    return function(request)
                else:
                    return redirect('/admin')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap

    def is_user_id(function):
        def wrap(request,id):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user']).filter(is_admin=0)) != 0:
                    return function(request,id)
                else:
                    return redirect('/admin')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap

    def is_logged_in_id(function):
        def wrap(request, id):
            # try:
            if 'user' in request.session:
                if len(User.objects.filter(id=request.session['user'])) != 0:
                    return function(request,id)
                else:
                    request.session.flush()
                    return redirect('/login')

            # except:
            else:
                messages.error(request, 'Timed Out')
                return redirect('/login')

        return wrap


    def is_guest(function):
        def wrap(request):
            if 'user' not in request.session:
                return function(request)
            else:
                return redirect('/index')

        return wrap
