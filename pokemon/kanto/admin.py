from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pokedex

# Register your models here.

@admin.register(Pokedex)
class PokedexAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']  # Anzuzeigende Felder in der Übersicht
    search_fields = ['name', 'type']  # Felder, nach denen gesucht werden kann