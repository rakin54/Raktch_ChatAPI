from django.urls import path
from .views import ChatView

urlpatterns = [
    path('api/posts/', ChatView.as_view(), name='chats'),
]
