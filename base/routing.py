from django.urls import re_path, path
from . import consumers

websocket_urlpatterns = [
   #  path('ws/court1/', consumers.CourtConsumer.as_asgi()),
  #   path('ws/court_one/', consumers.ScoreboardConsumer.as_asgi()),
   #  path('ws/court2/', consumers.CourtConsumer.as_asgi()),
   #  path('ws/court_two/', consumers.ScoreboardConsumer.as_asgi()),

   # WebSocket for CourtConsumer
    re_path(r'ws/court/(?P<court_name>\w+)/$', consumers.CourtConsumer.as_asgi()),

    # WebSocket for ScoreboardConsumer
    re_path(r'ws/scoreboard/(?P<court_name>\w+)/$', consumers.ScoreboardConsumer.as_asgi()),
]
