

# Create your models here.
from django.db import models

class MatchingRoom(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=100)
    max_participants = models.IntegerField()
    creator_phone = models.CharField(max_length=15)
    is_matching = models.BooleanField(default=True)

class Participant(models.Model):
    matching_room = models.ForeignKey(MatchingRoom, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
