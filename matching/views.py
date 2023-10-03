from django.shortcuts import render, redirect
from .models import MatchingRoom
from .models import Participant
from .forms import MatchingRoomForm, ParticipantForm

def create_matching_room(request):
    if request.method == 'POST':
        form = MatchingRoomForm(request.POST)
        if form.is_valid():
            matching_room = form.save()
            return render(request, 'matching_app/matching_created.html', {'matching_room': matching_room})
    else:
        form = MatchingRoomForm()
    return render(request, 'matching_app/create_matching_room.html', {'form': form})

def list_matching_rooms(request):
    matching_rooms = MatchingRoom.objects.filter(is_matching=True)
    return render(request, 'matching_app/list_matching_rooms.html', {'matching_rooms': matching_rooms})

def participate(request, matching_room_id):
    matching_room = MatchingRoom.objects.get(pk=matching_room_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.matching_room = matching_room
            participant.save()
            matching_room.is_matching = False
            matching_room.save()
            return render(request, 'matching_app/matching_completed.html')
    else:
        form = ParticipantForm()
    return render(request, 'matching_app/participate.html', {'form': form, 'matching_room': matching_room})

def show_map(request, matching_room_id):
    # Retrieve the matching room and its participants
    matching_room = MatchingRoom.objects.get(pk=matching_room_id)
    participants = Participant.objects.filter(matching_room=matching_room)

    # Calculate the center coordinates (e.g., the average of participant locations)
    center_lat = sum([participant.latitude for participant in participants]) / len(participants)
    center_lng = sum([participant.longitude for participant in participants]) / len(participants)

    context = {
        'center_lat': center_lat,
        'center_lng': center_lng,
        'participants': participants,
    }

    return render(request, 'matching_app/map.html', context)
