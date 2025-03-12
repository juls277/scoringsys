# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import CourtState


class CourtConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.court_name = self.scope['url_route']['kwargs']['court_name']
        self.room_group_name = f"court_{self.court_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Load or create the persistent state for this court
        state = await sync_to_async(CourtState.objects.get_or_create)(court_name=self.court_name)
        court_state, created = state  # unpack the tuple

        # Send the persistent state to the client
        await self.send(text_data=json.dumps({
            'player1_name': court_state.player1_name,
            'player1b_name': court_state.player1b_name,
            'player2_name': court_state.player2_name,
            'player2b_name': court_state.player2b_name,
            'player1_score': court_state.player1_score,
            'player2_score': court_state.player2_score,
            'current_set': court_state.current_set,
            'player1_set1': court_state.player1_set1,
            'player2_set1': court_state.player2_set1,
            'player1_set2': court_state.player1_set2,
            'player2_set2': court_state.player2_set2,
            'player1_set3': court_state.player1_set3,
            'player2_set3': court_state.player2_set3,
        }))

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Update the state in the persistent store
        await sync_to_async(CourtState.objects.filter(court_name=self.court_name).update)(
            player1_name=data.get('player1_name'),
            player1b_name=data.get('player1b_name'),
            player2_name=data.get('player2_name'),
            player2b_name=data.get('player2b_name'),
            player1_score=data.get('player1_score'),
            player2_score=data.get('player2_score'),
            current_set=data.get('current_set'),
            player1_set1=data.get('player1_set1'),
            player2_set1=data.get('player2_set1'),
            player1_set2=data.get('player1_set2'),
            player2_set2=data.get('player2_set2'),
            player1_set3=data.get('player1_set3'),
            player2_set3=data.get('player2_set3'),
        )

        # Broadcast the updated state to all connected clients
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'state_update',
                'data': data
            }
        )

    async def state_update(self, event):
        data = event['data']
        # Send the updated state to the WebSocket client
        await self.send(text_data=json.dumps(data))


class ScoreboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.court_name = self.scope['url_route']['kwargs']['court_name']
        self.group_name = f'court_{self.court_name}'

        # Add this connection to the court group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        print(f"Scoreboard WebSocket connected for court: {self.court_name}")

    async def disconnect(self, close_code):
        # Remove this connection from the court group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def score_update(self, event):
        # Send updated scores to the WebSocket client
        await self.send(text_data=json.dumps(event))
