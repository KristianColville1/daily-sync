from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$',
            consumers.ChatsConsumer.as_asgi()),
    re_path(r'wss/chat/(?P<room_name>\w+)/$',
            consumers.ChatsConsumer.as_asgi())
]
