from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PrivateMessage
from .views import PrivateMessageList


class PrivateMessageModelTest(APITestCase):
    def setUp(self):
        # Create two users and a message between them
        self.user1 = User.objects.create_user(
            username='user1', password='pass')
        self.user2 = User.objects.create_user(
            username='user2', password='pass')
        self.message = PrivateMessage.objects.create(
            sender=self.user1, recipient=self.user2, content='Test message')

    def test_str_method(self):
        # Test that the string representation of a message is its content
        self.assertEqual(str(self.message), self.message.content)

    def test_sender_field(self):
        # Test that the sender field of a message is set correctly
        self.assertEqual(self.message.sender, self.user1)

    def test_recipient_field(self):
        # Test that the recipient field of a message is set correctly
        self.assertEqual(self.message.recipient, self.user2)

    def test_content_field(self):
        # Test that the content field of a message is set correctly
        self.assertEqual(self.message.content, 'Test message')

    class PrivateMessageListTests(APITestCase):

        def setUp(self):
            # Create two users and two messages between them
            self.user1 = User.objects.create_user(
                username='user1', password='pass')
            self.user2 = User.objects.create_user(
                username='user2', password='pass')
            PrivateMessage.objects.create(
                sender=self.user1,
                recipient=self.user2,
                content='Test message 1')
            PrivateMessage.objects.create(
                sender=self.user2,
                recipient=self.user1,
                content='Test message 2')

        def test_get_list(self):
            # Test that a GET request to the private message list returns
            # all messages
            url = reverse('private_message_list')
            self.client.force_authenticate(user=self.user1)
            response = self.client.get(url)
            messages = PrivateMessage.objects.all()
            serializer = PrivateMessageSerializer(messages, many=True)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, serializer.data)
