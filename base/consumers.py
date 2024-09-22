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

        # Broadcast to the current court group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'score_update',
                'player1_name': data['player1_name'],
                'player2_name': data['player2_name'],
                'player1_score': data['player1_score'],
                'player2_score': data['player2_score'],
            }
        )

        # Broadcast the same data to the corresponding court (court1 <-> court_one)
        if self.court_name == 'court1':
            await self.channel_layer.group_send(
                'court_court_one',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_one':
            await self.channel_layer.group_send(
                'court_court1',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court2':
            await self.channel_layer.group_send(
                'court_court_two',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_two':
            await self.channel_layer.group_send(
                'court_court2',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court3':
            await self.channel_layer.group_send(
                'court_court_three',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_three':
            await self.channel_layer.group_send(
                'court_court3',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court4':
            await self.channel_layer.group_send(
                'court_court_four',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_four':
            await self.channel_layer.group_send(
                'court_court4',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court5':
            await self.channel_layer.group_send(
                'court_court_five',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_five':
            await self.channel_layer.group_send(
                'court_court5',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court6':
            await self.channel_layer.group_send(
                'court_court_six',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_six':
            await self.channel_layer.group_send(
                'court_court6',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court7':
            await self.channel_layer.group_send(
                'court_court_seven',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_seven':
            await self.channel_layer.group_send(
                'court_court7',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court8':
            await self.channel_layer.group_send(
                'court_court_eight',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_eight':
            await self.channel_layer.group_send(
                'court_court8',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court9':
            await self.channel_layer.group_send(
                'court_court_nine',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )
        elif self.court_name == 'court_nine':
            await self.channel_layer.group_send(
                'court_court9',
                {
                    'type': 'score_update',
                    'player1_name': data['player1_name'],
                    'player2_name': data['player2_name'],
                    'player1_score': data['player1_score'],
                    'player2_score': data['player2_score'],
                }
            )

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
