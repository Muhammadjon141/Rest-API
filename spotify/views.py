from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer
from .models import Albom, Artist, Song

class ArstistApiView(APIView):
    def get(self, request):
        search_data = request.query_params.get('search')
        query_set = Artist.get_info_artist()
        if search_data is not None:
            query_set = query_set.filter(first_name__icontains=search_data)
            serializers = ArtistSerializer(query_set, many=True)
            return Response(data=serializers.data)
        serializers = ArtistSerializer(query_set, many=True)
        return Response(data=serializers.data)
    
    def post(self, request):
        serializers = ArtistSerializer(data=request.data) 
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AlbomApiView(APIView):
    def get(self, request):
        search_data = request.query_params.get('search')
        query_set = Albom.get_info_albom()
        if search_data is not None:
            query_set = query_set.filter(title__icontains=search_data)
            serializers = AlbomSerializer(query_set, many=True)
            return Response(data=serializers.data)
        serializers = AlbomSerializer(query_set, many=True)
        return Response(data=serializers.data)
    
    def post(self, request):
        serializers = AlbomSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SongApiView(APIView):
    def get(self, request):
        search_data = request.query_params.get('search')
        query_set = Song.get_info_song()
        if search_data is not None:
            query_set = query_set.filter(title__icontains=search_data) | Song.get_full_name(search_data)
            serializers = SongSerializer(query_set, many=True)
            return Response(data=serializers.data)
        serializers = SongSerializer(query_set, many=True)
        return Response(data=serializers.data)
    
    def post(self, request):
        serializers = SongSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_201_CREATED)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SongDetailApiView(APIView):
    def get(self, request, id):
        song = Song.objects.get(id=id)
        serializers = SongSerializer(song)
        return Response(serializers.data)

    def put(self, request, id):
        song = Song.objects.get(id=id)
        serializers = SongSerializer(instance=song, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Song.objects.get(id=id)
        serializers = SongSerializer(instance=song, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        song = Song.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlbomDetailApiView(APIView):
    def get(self, request, id):
        albom = Albom.objects.get(id=id)
        serializers = AlbomSerializer(albom)
        return Response(serializers.data)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializers = AlbomSerializer(instance=albom, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializers = AlbomSerializer(instance=albom, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class ArtistDetailApiView(APIView):
    def get(self, request, id):
        artist = Artist.objects.get(id=id)
        serializers = ArtistSerializer(artist)
        return Response(serializers.data)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializers = ArtistSerializer(instance=artist, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializers = ArtistSerializer(instance=artist, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=status.HTTP_200_OK)
        return Response(data=serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)