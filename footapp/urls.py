from django.urls import path, include
from .api import ClubViewSet, PlayerViewSet
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('players/', views.player_list, name='player_list'),
    path('clubs/', views.club_list, name='club_list'),
    path('players/add/', views.add_player, name='add_player'),
    path('clubs/add/', views.add_club, name='add_club'),
    path('api/', include(router.urls)),
]
