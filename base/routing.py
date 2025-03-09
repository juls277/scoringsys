from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
   # WebSocket for CourtConsumer
    re_path(r'wss/court/(?P<court_name>\w+)/$', consumers.CourtConsumer.as_asgi()),

    # WebSocket for ScoreboardConsumer
    re_path(r'wss/scoreboard/(?P<court_name>\w+)/$', consumers.ScoreboardConsumer.as_asgi()),
]
