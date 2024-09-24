import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CourtConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.court_name = self.scope['url_route']['kwargs']['court_name']
        self.group_name = f'court_{self.court_name}'

        # Add this connection to the correct court group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        print(f"WebSocket connection established for court: {self.court_name}")

    async def disconnect(self, close_code):
        # Remove this connection from the group
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        print(f"WebSocket connection closed for court: {self.court_name}, code: {close_code}")

    async def receive(self, text_data):
    # Parse the incoming data
        data = json.loads(text_data)

    # Prepare the payload with the current set and all sets for both players
        message = {
        'type': 'score_update',
        'player1_name': data['player1_name'],
        'player2_name': data['player2_name'],
        'player1_score': data['player1_score'],
        'player2_score': data['player2_score'],
        'current_set': data['current_set'],
        'player1_set1': data['player1_set1'],
        'player1_set2': data['player1_set2'],
        'player1_set3': data['player1_set3'],
        'player2_set1': data['player2_set1'],
        'player2_set2': data['player2_set2'],
        'player2_set3': data['player2_set3'],
    }

    # Broadcast to the current court group
        await self.channel_layer.group_send(self.group_name, message)

    # Broadcast the same data to the corresponding court (court1 <-> court_one)
        if self.court_name == 'court1':
            await self.channel_layer.group_send('court_court_one', message)
        elif self.court_name == 'court_one':
            await self.channel_layer.group_send('court_court1', message)
        elif self.court_name == 'court2':
            await self.channel_layer.group_send('court_court_two', message)
        elif self.court_name == 'court_two':
            await self.channel_layer.group_send('court_court2', message)
        elif self.court_name == 'court3':
            await self.channel_layer.group_send('court_court_three', message)
        elif self.court_name == 'court_three':
            await self.channel_layer.group_send('court_court3', message)
        elif self.court_name == 'court4':
            await self.channel_layer.group_send('court_court_four', message)
        elif self.court_name == 'court_four':
            await self.channel_layer.group_send('court_court4', message)
        elif self.court_name == 'court5':
            await self.channel_layer.group_send('court_court_five', message)
        elif self.court_name == 'court_five':
            await self.channel_layer.group_send('court_court5', message)
        elif self.court_name == 'court6':
            await self.channel_layer.group_send('court_court_six', message)
        elif self.court_name == 'court_six':
            await self.channel_layer.group_send('court_court6', message)
        elif self.court_name == 'court7':
            await self.channel_layer.group_send('court_court_seven', message)
        elif self.court_name == 'court_seven':
            await self.channel_layer.group_send('court_court7', message)
        elif self.court_name == 'court8':
            await self.channel_layer.group_send('court_court_eight', message)
        elif self.court_name == 'court_eight':
            await self.channel_layer.group_send('court_court8', message)
        elif self.court_name == 'court9':
            await self.channel_layer.group_send('court_court_nine', message)
        elif self.court_name == 'court_nine':
            await self.channel_layer.group_send('court_court9', message)


    async def score_update(self, event):
        # Send updated scores to the WebSocket client
        await self.send(text_data=json.dumps(event))



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