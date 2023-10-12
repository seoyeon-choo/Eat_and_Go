from django.shortcuts import render,get_object_or_404, HttpResponseRedirect,  redirect
from .forms import MatchingRoomForm, ParticipantForm
from .models import MatchingRoom, Participant, Chat
from .forms import ChatForm


def chat(request, matching_room_id):
    participants = Participant.objects.filter(matching_room__id=matching_room_id)

    if participants.count() == 1:
        participant = participants.first()
        matching_room = participant.matching_room
        chat_messages = Chat.objects.filter(participant=participant).order_by('timestamp')

        if request.method == 'POST':
            form = ChatForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.participant = participant
                #message.sender = request.user.username  # You can change this to the actual sender's name
                message.sender = " 나 "
                message.save()
                return redirect('matching_app:chat', matching_room_id=matching_room_id)

        else:
            form = ChatForm()

        return render(request, 'matching_app/chat.html', {
            'matching_room': matching_room,
            'chat_messages': chat_messages,
            'form': form,
        })
    else:
        # Handle the case of multiple participants in the matching room
        return render(request, 'matching_app/multiple_participants.html')


def create_matching_room(request):
    if request.method == 'POST':
        form = MatchingRoomForm(request.POST)
        if form.is_valid():
            form.save()
            #matching_room = form.save()
            return HttpResponseRedirect('/matching_app/list_matching_rooms/')
            #return render(request, 'matching_app/matching_created.html', {'matching_room': matching_room})
    else:
        form = MatchingRoomForm()
    context={'form': form}
    return render(request, 'matching_app/create_matching_room.html', context)


def list_matching_rooms(request):
    matching_rooms = MatchingRoom.objects.all()
    context = {'matching_rooms': matching_rooms}
    return render(request, 'matching_app/list_matching_rooms.html', context)


def list_matching_rooms(request):
    sort_by = request.GET.get('sort-by', 'created')  # Default to 'created' if no option selected

    if sort_by == 'time-left':
        matching_rooms = MatchingRoom.objects.all().order_by('time')
    else:
        matching_rooms = MatchingRoom.objects.all().order_by('-time')

    context = {'matching_rooms': matching_rooms}
    return render(request, 'matching_app/list_matching_rooms.html', context)


def participate(request, matching_room_id):
    #matching_room = MatchingRoom.objects.get(pk=matching_room_id)
    matching_room = get_object_or_404(MatchingRoom, pk=matching_room_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            #check if the room is fuul
            if matching_room.participants_count >= matching_room.max_participants:
                return render(request, 'matching_app/room_full.html',{'matching_room': matching_room})
            #save the participant and update matching_room
            participant = form.save(commit=False)
            participant.matching_room = matching_room
            participant.save()

            # Increment participants count for the matching room
            matching_room.participants_count += 1
            matching_room.save()

            # Check if the room is now full
            if matching_room.participants_count >= matching_room.max_participants:
                matching_room.is_matching = False
                matching_room.save()

            return render(request, 'matching_app/matching_completed.html', {'matching_room': matching_room})
    else:
        form = ParticipantForm()
    return render(request, 'matching_app/participate.html', {'form': form, 'matching_room': matching_room})

def matching_completed(request, matching_room_id):
    # Retrieve the matching room based on matching_room_id
    matching_room = MatchingRoom.objects.get(pk=matching_room_id)

    context = {
        'matching_room': matching_room,
    }
    return render(request, 'matching_app/matching_completed.html', context)


def show_map(request, matching_room_id):
    # Retrieve the matching room and its participants
    matching_room = MatchingRoom.objects.get(pk=matching_room_id)
    participants = Participant.objects.filter(matching_room=matching_room)

    # Create a list of dictionaries containing latitude and longitude for each participant
    # duksung women's universtiy lat and lng location
    participant_data = [
        #{'lat': participant.lat, 'lng': participant.lng, 'name': participant.participant_name}
        {'lat': 37.651712, 'lng': 127.016956}
        for participant in participants
    ]

    # Calculate the center coordinates (e.g., the average of participant locations)
    center_lat = sum([37.651712 for participant in participants]) / len(participants)
    center_lng = sum([127.016956 for participant in participants]) / len(participants)

    # Include your own location in participant_data
    # duksung women's university lat and lng
    your_location = {'lat':37.651223644611, 'lng': 127.01329681375}  # Replace with your actual latitude and longitude
    participant_data.append(your_location)

    context = {
        'center_lat': center_lat,
        'center_lng': center_lng,
        'participants': participants,
    }

    return render(request, 'matching_app/map.html', context)

