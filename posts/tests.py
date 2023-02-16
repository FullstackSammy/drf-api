from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Post


class PostModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='password')
        self.post = Post.objects.create(
            owner=self.user,
            title='Test Post',
            content='Test Content',
            image='../default_post_yz9h7i'
        )

    def test_post_creation(self):
        """
        Test that a Post instance can be created and saved to the database
        """
        post = Post.objects.create(
            owner=self.user,
            title='New Post',
            content='New Content',
            image='../default_post_yz9h7i'
        )
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(Post.objects.last().title, 'Test Post')

    def test_post_deletion(self):
        """
        Test that a Post instance can be deleted from the database
        """
        self.post.delete()
        self.assertEqual(Post.objects.count(), 0)

    def test_post_update(self):
        """
        Test that a Post instance can be updated
        """
        self.post.title = 'Updated Title'
        self.post.content = 'Updated Content'
        self.post.save()
        self.assertEqual(
            Post.objects.get(id=self.post.id).title, 'Updated Title')
        self.assertEqual(
            Post.objects.get(id=self.post.id).content, 'Updated Content')
