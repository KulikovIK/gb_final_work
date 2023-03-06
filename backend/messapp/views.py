from rest_framework.viewsets import ModelViewSet

from .models import Message
from .serializer import MessageSerializer


class MessageModelViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

