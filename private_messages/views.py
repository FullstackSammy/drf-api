from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import PrivateMessage
from .serializer import PrivateMessageSerializer


class PrivateMessageList(generics.ListCreateAPIView):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class PrivateMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrivateMessage.objects.all()
    serializer_class = PrivateMessageSerializer
    permission_classes = [IsAuthenticated]
