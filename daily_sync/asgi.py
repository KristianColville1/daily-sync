import os
import chats.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "daily_sync.settings")
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.

application = ProtocolTypeRouter({
    "http":
    get_asgi_application(),
    "websocket":
    AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(chats.routing.websocket_urlpatterns))),
})
