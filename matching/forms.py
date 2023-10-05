from django import forms
from .models import MatchingRoom,Participant

class MatchingRoomForm(forms.ModelForm):
    class Meta:
        model = MatchingRoom
        fields = ['subject', 'content', 'time', 'place', 'max_participants', 'creator_phone']

        labels = {
            'subject': '제목',
            'content': '내용',
            'time': '시간',
            'place': '장소',
            'max_participants': '최대 인원',
            'creator_phone': '전화번호',
        }

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['phone_number']
