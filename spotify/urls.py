from django.urls import path
from .views import ArstistApiView, AlbomApiView, SongApiView, SongDetailApiView, AlbomDetailApiView, ArtistDetailApiView

urlpatterns = [
    path('artist/', ArstistApiView.as_view(), name='ArstistApiView'),
    path('artist/<int:id>/', ArtistDetailApiView.as_view(), name='ArstistApiView_detail'),
    path('albom/', AlbomApiView.as_view(), name='AlbomApiView'),
    path('albom/<int:id>/', AlbomDetailApiView.as_view(), name='AlbomApiView_detail'),
    path('song/', SongApiView.as_view(), name='SongApiView'),
    path('song/<int:id>/', SongDetailApiView.as_view(), name='SongApiView_detail'),
]