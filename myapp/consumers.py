import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

from .models import  allDevices ,deviceStatus

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        d_id = data['d_id']
        pins1status = data['pin1Status']
        pins2status=data['pin2Status']
        pins3status=data['pin3Status']
        pins4status=data['pin4Status']
        pins5status=data['pin5Status']
        pins6status=data['pin6Status']
        pins7status=data['pin7Status']
        pins8status=data['pin8Status']
        pins9status=data['pin9Status']
        pins10status=data['pin10Status']
        
        # sensor1=data['sensor1']
        # sensor2=data['sensor2']
        # sensor3=data['sensor3']
        # sensor4=data['sensor4']
        # sensor5=data['sensor5']
        # sensor6=data['sensor6']
        # sensor7=data['sensor7']
        # sensor8=data['sensor8']
        # sensor9=data['sensor9']
        # sensor10=data['sensor10']
        # username = data['username']
        # room = data['room']

        await self.save_message(d_id, data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                 'd_id':d_id,
                'pin1Status': pins1status,
                'pin2Status': pins2status,
                'pin3Status': pins3status,
                'pin4Status': pins4status,
                'pin5Status': pins5status,
                'pin6Status': pins6status,
                'pin7Status': pins7status,
                'pin8Status': pins8status,
                'pin9Status': pins9status,
                'pin10Status': pins10status,
                
                # 'sensor1': sensor1,
                # 'sensor2': sensor2,
                # 'sensor3': sensor3,
                # 'sensor4': sensor4,
                # 'sensor5': sensor5,
                # 'sensor6': sensor6,
                # 'sensor7': sensor7,
                # 'sensor8': sensor8,
                # 'sensor9': sensor9,
                # 'sensor10': sensor10,

                
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        d_id=event['d_id']
        pin1status = event['pin1Status']
        pin2status = event['pin2Status']
        pin3status = event['pin3Status']
        pin4status = event['pin4Status']
        pin5status = event['pin5Status']
        pin6status = event['pin6Status']
        pin7status = event['pin7Status']
        pin8status = event['pin8Status']
        pin9status = event['pin9Status']
        pin10status = event['pin10Status']
        
        # sensor1 = event['sensor1']
        # sensor2 = event['sensor2']
        # sensor3 = event['sensor3']
        # sensor4 = event['sensor4']
        # sensor5 = event['sensor5']
        # sensor6 = event['sensor6']
        # sensor7 = event['sensor7']
        # sensor8 = event['sensor8']
        # sensor9 = event['sensor9']
        # sensor10 = event['sensor10']

       

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'd_id':d_id,
              'pin1Status': pin1status,
                'pin2Status': pin2status,
                'pin3Status': pin3status,
                'pin4Status': pin4status,
                'pin5Status': pin5status,
                'pin6Status': pin6status,
                'pin7Status': pin7status,
                'pin8Status': pin8status,
                'pin9Status': pin9status,
                'pin10Status': pin10status,
                
                # 'sensor1': sensor1,
                # 'sensor2': sensor2,
                # 'sensor3': sensor3,
                # 'sensor4': sensor4,
                # 'sensor5': sensor5,
                # 'sensor6': sensor6,
                # 'sensor7': sensor7,
                # 'sensor8': sensor8,
                # 'sensor9': sensor9,
                # 'sensor10': sensor10,

            
            
        }))
    @sync_to_async
    def save_message(self, d_id, data):
        d_id = allDevices(d_id=d_id)
        if deviceStatus.objects.filter(d_id=d_id).exists:
            # df = healthrecord.objects.filter(d_id=d_id)
            # dfJson = recordhealthSerializers(df, many=True)
            t = deviceStatus.objects.get(d_id=d_id)

            t.pin1Status =data['pin1Status']
            t.pin2Status = data['pin2Status']
            t.pin3Status = data['pin3Status']
            t.pin4Status = data['pin4Status']
            t.pin5Status = data['pin5Status']
            t.pin6Status = data['pin6Status']
            t.pin7Status = data['pin7Status']
            t.pin8Status = data['pin8Status']
            t.pin9Status = data['pin9Status']
            t.pin10Status = data['pin10Status']
            
            # t.sensor1 = data['sensor1']
            # t.sensor2 = data['sensor2']
            # t.sensor3 = data['sensor3']
            # t.sensor4 = data['sensor4']
            # t.sensor5 = data['sensor5']
            # t.sensor6 = data['sensor6']
            # t.sensor7 = data['sensor7']
            # t.sensor8 = data['sensor8']
            # t.sensor9 = data['sensor9']
            # t.sensor10 = data['sensor10']
            t.save()
            print("updated")
        else:
            deviceStatus.objects.create(d_id=d_id,t=data)
            print("created...!!!")

    # @sync_to_async
    # def save_message(self, username, room, sensor1,sensor2):
    #     Message.objects.create(username=username, room=room,sensor1=sensor1,sensor2=sensor2)