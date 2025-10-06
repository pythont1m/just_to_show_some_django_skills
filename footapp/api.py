from rest_framework import viewsets
from .models import Players, Clubs
from .serializers import PlayersSerializer, ClubsSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Clubs.objects.all()
    serializer_class = ClubsSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
