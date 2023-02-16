from django.urls import path
from .views import PrivateMessageList, PrivateMessageDetail

urlpatterns = [
    path('messages/', PrivateMessageList.as_view(), name='message-list'),
    path('messages/<int:pk>', PrivateMessageDetail().as_view(), name='message-detail'),
]
