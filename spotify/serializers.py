from .models import Albom, Artist, Song
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbomSerializer(serializers.ModelSerializer):
    author=ArtistSerializer()
    class Meta:
        model = Albom
        fields = '__all__'

class SongSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    albom = AlbomSerializer()
    
    class Meta:
        model = Song
        fields = '__all__'