from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('chat/<str:username>/', views.ChatHistoryView.as_view(), name='chat-history'),
]