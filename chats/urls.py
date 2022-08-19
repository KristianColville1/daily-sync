from django.urls import path
from . import views

urlpatterns = [
    path('', views.ChatView.as_view(), name='chat'),
    path('<str:room_name>/', views.ChatRoomView.as_view(), name='room')
]
