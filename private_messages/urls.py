from django.urls import path
from private_messages import views
from .views import MessageViewSet

# Use `.as_view()` with the `actions` argument to specify allowed HTTP methods
message_list = MessageViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

message_detail = MessageViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('private_messages/', message_list, name='message-list'),
    path('private_messages/<int:pk>/', message_detail, name='message-detail'),
]