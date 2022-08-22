from django.shortcuts import render
from django.views import View


class ChatView(View):
    """
    ChatView
    """

    def get(self, request):
        return render(request, 'chats/index.html')


class ChatRoomView(View):
    """
    ChatRoomView
    """

    def get(self, request, room_name):
        context = {
            'room_name': room_name,
        }
        return render(request, 'chats/room.html', context)
