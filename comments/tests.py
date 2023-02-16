from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from .models import Comment


class CommentModelTest(APITestCase):
    def setUp(self):
        # Create a user and a post for the comment
        self.user = User.objects.create_user(username='user', password='pass')
        self.post = Post.objects.create(
            title='Test post', content='Test content', owner=self.user)

    def test_str_method(self):
        # Test that the string representation of a comment is its content
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment')
        self.assertEqual(str(comment), comment.content)

    def test_owner_field(self):
        # Test that the owner field of a comment is set correctly
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment')
        self.assertEqual(comment.owner, self.user)

    def test_post_field(self):
        # Test that the post field of a comment is set correctly
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment')
        self.assertEqual(comment.post, self.post)

    def test_content_field(self):
        # Test that the content field of a comment is set correctly
        comment = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment')
        self.assertEqual(comment.content, 'Test comment')

    def test_ordering(self):
        # Test that comments are ordered by descending creation date
        comment1 = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment 1')
        comment2 = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment 2')
        comment3 = Comment.objects.create(
            owner=self.user, post=self.post, content='Test comment 3')
        comments = Comment.objects.all()
        self.assertEqual(comments[0], comment3)
        self.assertEqual(comments[1], comment2)
        self.assertEqual(comments[2], comment1)
