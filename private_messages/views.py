from rest_framework import viewsets, permissions
from .models import Message
from .serializers import MessageSerializer

# Create your views here.
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializers_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
    
    def get_queryset(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)