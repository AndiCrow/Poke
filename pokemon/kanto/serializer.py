from rest_framework import serializers
from .models import Pokedex

class PokedexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokedex
        fields = ['id', 'name', 'type']