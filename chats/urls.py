from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.ChatView.as_view()), name='chat'),
    path('<str:room_name>/', login_required(views.ChatRoomView.as_view()), name='room')
]
