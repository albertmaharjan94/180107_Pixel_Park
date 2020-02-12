"""PixelPark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pixel_park_django.views import UserView, HomeView, PostView
from pixel_park_django.views.Admin import DashView, A_UserView, A_PostView

urlpatterns = [
    # path('test', UserView.index),

    # Landing Views
    path('login', UserView.login),
    path('logged', UserView.logged),
    path('register', UserView.register),
    path('register/store', UserView.store),
    path('hasEmail', UserView.hasEmail),
    path('hasUsername', UserView.hasUsername),

    # Home views
    path('index/', HomeView.index),
    path('logout', HomeView.logout),
    path('profile/<int:id>', HomeView.profile),
    path('profile/post/<int:id>', HomeView.profile_photo),

    path('profile/comment', HomeView.comment),

    # likes ajax
    path('profile/post/like/<int:post_id>/<int:user_id>', HomeView.profile_like),
    path('profile/post/unlike/<int:post_id>/<int:user_id>', HomeView.profile_unlike),

    # Change profile image of a user
    path('profile/image-update/<int:id>', HomeView.profile_image_update),

    #
    path('profile/follower/<int:id>', HomeView.follower_list),
    path('profile/following/<int:id>', HomeView.following_list),

    path('profile/like/<int:id>', HomeView.like_list),

    path('profile/follow', HomeView.follow_profile),
    path('profile/unfollow', HomeView.unfollow_profile),

    # sesarch
    path('profile/search', HomeView.search),

    # get notification
    path('profile/get-notification', HomeView.get_notification),

    # Post views
    path('upload', PostView.upload),

    path('forget', UserView.forget),

    path('profile/<int:id>/edit', UserView.edit_user),

    path('profile/<int:id>/update', UserView.update_user),
    path('post/delete/<int:id>', PostView.delete_post),

    # path('admin/', admin.site.urls),
    path('admin/', DashView.index),

    path('admin/users', A_UserView.index),
    path('admin/user/delete', A_UserView.delete),
    path('admin/user/create', A_UserView.create),
    path('admin/users', A_UserView.create),
    path('admin/user/edit/<int:id>', A_UserView.edit),

    path('admin/user/edit-password/<int:id>', A_UserView.edit_password),
    path('admin/users/update/<int:id>', A_UserView.update),
    path('admin/users/update-password/<int:id>', A_UserView.update_password),

    path('admin/posts', A_PostView.index),
    path('admin/post/delete', A_PostView.delete),
    path('admin/post/edit/<int:id>', A_PostView.edit),
    path('admin/post/update/<int:id>', A_PostView.update),
    path('admin/post/create', A_PostView.create),
    path('admin/post/store', A_PostView.store),

    path('admin/posts/comment/delete', A_PostView.comment_delete),
    path('admin/posts/comments/<int:id>', A_PostView.comment),

    path('admin/post/edit-comment/<int:id>', A_PostView.comment_edit),
    path('admin/post/comment/update/<int:id>',A_PostView.comment_update),
    path('admin/post/comment/create/<int:id>',A_PostView.comment_create),

    path('admin/post/comment/store/<int:id>', A_PostView.comment_store),
]
