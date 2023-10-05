from django.db import models

class MatchingRoom(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    place = models.CharField(max_length=100)
    max_participants = models.IntegerField()
    creator_phone = models.CharField(max_length=15)
    create_date = models.DateTimeField()
    is_matching = models.BooleanField(default=True)

class Participant(models.Model):
    matching_room = models.ForeignKey(MatchingRoom, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

class Images(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
