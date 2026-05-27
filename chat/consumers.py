import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import timezone

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.canal_id = self.scope['url_route']['kwargs']['canal_id']
        self.canal_group = f'chat_{self.canal_id}'
        await self.channel_layer.group_add(self.canal_group, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.canal_group, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        mensagem = data.get('mensagem', '')
        usuario = self.scope['user']
        if not usuario.is_authenticated or not mensagem.strip():
            return
        await self.salvar_mensagem(usuario, mensagem)
        await self.channel_layer.group_send(self.canal_group, {
            'type': 'chat_message',
            'mensagem': mensagem,
            'usuario': usuario.get_full_name() or usuario.username,
            'usuario_id': usuario.id,
            'hora': timezone.now().strftime('%H:%M'),
        })

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def salvar_mensagem(self, usuario, conteudo):
        from .models import Mensagem, Canal
        try:
            canal = Canal.objects.get(pk=self.canal_id)
            Mensagem.objects.create(canal=canal, remetente=usuario, conteudo=conteudo)
        except Canal.DoesNotExist:
            pass
