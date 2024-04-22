from django.urls import path
from . import views

urlpatterns = [
    path('pokedex/', views.PokedexListCreateAPIView.as_view(), name='pokedex-list'),
    path('pokedex/<int:pk>/', views.PokedexRetrieveUpdateAPIView.as_view(), name='pokedex-update'),
]