from .models import playlist
from .serializers import PlaylistSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
class PlaylistListView(ListCreateAPIView):
    queryset = playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(RetrieveUpdateDestroyAPIView):
    queryset = playlist.objects.all()
    serializer_class = PlaylistSerializer