from django import forms
from .models import MatchingRoom,Participant
from .models import Chat

class MatchingRoomForm(forms.ModelForm):
    class Meta:
        model = MatchingRoom
        fields = ['time', 'place', 'max_participants', 'creator_phone', 'subject', 'context']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['phone_number']

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ['message']