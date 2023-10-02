from django import forms
from .models import MatchingRoom,Participant

class MatchingRoomForm(forms.ModelForm):
    class Meta:
        model = MatchingRoom
        fields = ['time', 'place', 'max_participants', 'creator_phone']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['phone_number']
