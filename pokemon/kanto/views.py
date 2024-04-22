from django.shortcuts import render
from .models import Pokedex
from .serializer import PokedexSerializer
from rest_framework import generics
# Create your views here.


class PokedexListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer

class PokedexRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer