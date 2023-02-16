from django.urls import path
from .views import PrivateMessageList, PrivateMessageDetail

urlpatterns = [
    path('', PrivateMessageList.as_view(), name='private_message_list'),
    path('<int:pk>/', PrivateMessageDetail.as_view(), name='private_message_detail'),
]
