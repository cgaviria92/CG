from django.contrib.auth.models import User
from django.db import models
from django.db.models import JSONField
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.PositiveIntegerField(default=0)
    currency = models.PositiveIntegerField(default=100)
    current_ship = models.ForeignKey('Ship', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Ship(models.Model):
    name = models.CharField(max_length=50)
    health = models.PositiveIntegerField(default=100)
    damage = models.PositiveIntegerField(default=10)
    speed = models.PositiveIntegerField(default=5)
    price = models.PositiveIntegerField(default=50)

    def __str__(self):
        return self.name



class Map(models.Model):
    name = models.CharField(max_length=50)
    width = models.PositiveIntegerField(default=1000)
    height = models.PositiveIntegerField(default=1000)
    map_data = JSONField(default=dict)  # JSON para datos como posiciones de elementos.

    def __str__(self):
        return self.name
class NPC(models.Model):
    name = models.CharField(max_length=50)
    health = models.PositiveIntegerField(default=50)
    damage = models.PositiveIntegerField(default=5)
    position_x = models.PositiveIntegerField(default=0)
    position_y = models.PositiveIntegerField(default=0)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='npcs')

    def __str__(self):
        return self.name
