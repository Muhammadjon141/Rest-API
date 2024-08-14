from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArstistApiViewSet, AlbomApiViewSet, SongApiViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'artist', ArstistApiViewSet, basename='artist')
router.register(r'albom', AlbomApiViewSet, basename='albom')
router.register(r'song', SongApiViewSet, basename='song')


urlpatterns = [
    # path('', include(router.urls)),
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]