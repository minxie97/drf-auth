from rest_framework import generics
from .serializer import GameSerializer
from .models import Game
from .permissions import IsOwnerOrReadOnly

class GameList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer