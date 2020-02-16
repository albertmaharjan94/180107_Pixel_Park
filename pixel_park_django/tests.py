from django.test import TestCase
from .models.Post import Post
from .models.User import User
from .models.Comment import Comment


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(name="albert", username="test.user", email="test@gmail.com", is_admin=0)
        user2 = User.objects.create(name="test", username="test2.user", email="test2@gmail.com", is_admin=0)
        Post.objects.create(caption="This is a test post", user_id=user.id)

    def test_user(self):
        user = User.objects.get(username="test.user")
        self.assertEqual(user.email, 'test@gmail.com')

    def test_Post(self):
        post = Post.objects.get(caption="This is a test post")
        self.assertEqual(post.user.name, 'albert')

    def test_Comment(self):
        user2 = User.objects.get(username="test2.user")
        user = User.objects.get(username="test.user")
        post = Post.objects.get(caption="This is a test post")
        comment = Comment.objects.create(post_id=post.id, user_id=user2.id)

        self.assertEqual(comment.user.id, user2.id)
