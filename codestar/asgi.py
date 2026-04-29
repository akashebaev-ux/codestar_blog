import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import chatbox.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codestar.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    # 👇 THIS enables WebSockets
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chatbox.routing.websocket_urlpatterns
        )
    ),
})