from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import music
from .serializers import MusicSerializer
from django.shortcuts import get_object_or_404

# Create your views here.
class MusicListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        songs = music.objects.all()
        serialized_songs = MusicSerializer(songs, many=True)
        return Response(serialized_songs.data)

    def post(self, request):
        serialized_songs  = MusicSerializer(data=request.data)
        if serialized_songs.is_valid(raise_exception=True):
            serialized_songs.save()
            return Response(serialized_songs.data, 201)

class MusicDetailView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, pk):
        song = get_object_or_404(music, pk=pk)
        serialized_songs  = MusicSerializer(song)
        return Response(serialized_songs.data)

    def put(self, request, pk):
        song = get_object_or_404(music, pk=pk)
        serialized_songs  = MusicSerializer(song, data=request, partial=True)
        serialized_songs.is_valid(raise_exception=True)
        song.save()
        return Response(serialized_songs.data)

    def delete(self, request, pk):
        song = get_object_or_404(music, pk=pk)
        song.delete()
        return Response(status=204)