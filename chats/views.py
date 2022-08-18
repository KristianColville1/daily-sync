from django.shortcuts import render
from django.views import View


class ChatView(View):
    """
    ChatView
    """
    def get(self, request):
        return render(request, 'chats/index.html')
