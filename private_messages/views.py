from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PrivateMessage
from .serializers import PrivateMessageSerializer


class PrivateMessageList(generics.ListCreateAPIView):
    """
    View for listing and creating private messages
    """
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Method that sets the sender field to the authenticated user,
        when creating a new PrivateMessage object.
        """
        serializer.save(sender=self.request.user)


class PrivateMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting individual private messages.
    """
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [IsAuthenticated]
