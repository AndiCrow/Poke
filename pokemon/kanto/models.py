from django.db import models

# Create your models here.

class Pokedex(models.Model):
    name = models.CharField(max_length=100)
    TYPE_CHOICES = [
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('electric', 'Electric'),
        ('flying', 'Flying'),
        ('normal', 'Normal'),
        ('ice', 'Ice'),
        ('psychic', 'Psychic'),
        ('poisen', 'Poison'),
        ('fighting', 'Fighting'),
        ('dragon', 'Dragon'),
        ('ghost', 'Ghost'),
        ('dark', 'Dark'),
        ('ground', 'Ground'),
        ('fairy', 'Fairy'),
        ('rock', 'Rock'),
        ('bug', 'Bug'),
        ('grass', 'Grass'),
        ('steel', 'Steel'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
