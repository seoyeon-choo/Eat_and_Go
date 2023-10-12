# Create your models here.
from django.db import models

class MatchingRoom(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=100)
    max_participants = models.PositiveIntegerField()
    participants_count = models.PositiveIntegerField(default = 1)
    creator_phone = models.CharField(max_length=15)
    is_matching = models.BooleanField(default=True)
    subject = models.CharField(max_length=100, default="Default Subject")  # New field for subject
    context = models.TextField(default="Default Context")  # New field for context

    def __str__(self):
        return self.title

class Participant(models.Model):
    matching_room = models.ForeignKey(MatchingRoom, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number

class Chat(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    sender = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}: {self.message}'
