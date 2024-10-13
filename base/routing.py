from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
   #  path('wss/court1/', consumers.CourtConsumer.as_asgi()),
  #   path('wss/court_one/', consumers.ScoreboardConsumer.as_asgi()),
   #  path('ws/court2/', consumers.CourtConsumer.as_asgi()),
   #  path('ws/court_two/', consumers.ScoreboardConsumer.as_asgi()),

   # WebSocket for CourtConsumer
    re_path(r'wss/court/(?P<court_name>\w+)/$', consumers.CourtConsumer.as_asgi()),

    # WebSocket for ScoreboardConsumer
    re_path(r'wss/scoreboard/(?P<court_name>\w+)/$', consumers.ScoreboardConsumer.as_asgi()),
]
