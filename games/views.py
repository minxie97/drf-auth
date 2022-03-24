from rest_framework import generics
from .serializer import GameSerializer
from .models import Game
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated

class GameList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer