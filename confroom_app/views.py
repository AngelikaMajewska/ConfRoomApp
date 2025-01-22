
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime, date, timedelta
from confroom_app.models import Room, Booking


# Create your views here.
class AddRoom(View):
    def get(self, request):
        return render(request, 'confroom_app/add_room.html')
    def post(self, request):
        room_name = request.POST['name']
        room_capacity = request.POST['capacity']
        projector = request.POST.get('has_projector') == "on"
        current_confroom = Room.objects.values_list('name', flat=True)
        if room_name != "":
            if room_name in current_confroom:
                response = "Room already exists"
                return render(request, 'confroom_app/add_room.html', {"response": response,'capacity':room_capacity, 'projector':projector})
        else:
            response = "Room name cannot be empty"
            return render(request, 'confroom_app/add_room.html', {"response": response,'capacity':room_capacity, 'projector':projector})

        if room_capacity != "":
            try:
                room_capacity = int(room_capacity)
            except ValueError:
                response = "Capacity must be an integer"
                return render(request, 'confroom_app/add_room.html', {"response": response, 'name':room_name, 'projector':projector})
            if room_capacity <= 0:
                response = "Capacity must be greater than 0"
                return render(request, 'confroom_app/add_room.html', {"response": response, 'name':room_name, 'projector':projector})
        else:
            response = "Capacity cannot be empty"
            return render(request, 'confroom_app/add_room.html', {"response": response, 'name':room_name, 'projector':projector})

        Room.objects.create(name=room_name, capacity=room_capacity, has_projector=projector)
        response = "Room added"
        return render(request, 'confroom_app/add_room.html', {"response": response})

from django.db.models import Exists, OuterRef, UniqueConstraint


class Homepage(View):
    def get(self, request):
        today = (datetime.today().date()).strftime("%Y-%m-%d")
        all_rooms = Room.objects.annotate(
            is_booked=Exists(
                Booking.objects.filter(room=OuterRef('pk'), date=today)
            )
        )
        return render(request, 'confroom_app/homepage.html', {'all_rooms': all_rooms, 'today': today})

class DeleteRoom(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        room.delete()
        return redirect('search-rooms')

class ModifyRoom(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        return render(request, 'confroom_app/modify_room.html', {'room': room})
    def post(self, request, room_id):
        room_name = request.POST['name']
        room_capacity = request.POST['capacity']
        room_has_projector = 'has_projector' in request.POST

        current_confroom = Room.objects.values_list('name', flat=True)
        room = Room.objects.get(pk=room_id)

        if room_name != "" and room_name != room.name:
            if room_name in current_confroom:
                return HttpResponse("Room name already exists")
        elif room_name != "" and room_name == room.name:
            pass
        else:
            return HttpResponse("Room name cannot be empty")

        if room_capacity != "":
            try:
                room_capacity = int(room_capacity)
            except ValueError:
                return HttpResponse("Capacity must be an integer")
            if room_capacity <= 0:
                return HttpResponse("Capacity must be greater than 0")
        else:
            return HttpResponse("Capacity cannot be empty")

        room.name = room_name
        room.capacity = room_capacity
        room.has_projector = room_has_projector
        room.save()
        return redirect('search-rooms')

class BookRoom(View):
    def get(self, request, room_id):
        room = get_object_or_404(Room, pk=room_id)
        bookings = Booking.objects.filter(room=room, date__gte=date.today())
        for booking in bookings:
            booking.date = booking.date.strftime('%d-%m-%Y')
        data_available = None if len(bookings) == 0 else 1
        return render(request, 'confroom_app/booking.html', {'room': room, 'bookings':bookings ,'data_available': data_available})

    def post(self, request, room_id):
        date = datetime.strptime(request.POST['date'], "%Y-%m-%d").date()
        room = get_object_or_404(Room, pk=room_id)
        comment = request.POST['comment']
        dates = Booking.objects.values_list('date', flat=True)
        dates_cleaned = [date.strftime("%Y-%m-%d") for date in dates]
        if date not in dates_cleaned:
            if date >= datetime.today().date():
                try:
                    Booking.objects.create(date=date, comment=comment, room=room)
                except Exception:
                    room = get_object_or_404(Room, pk=room_id)
                    bookings = Booking.objects.filter(room=room, date__gte=date.today())
                    for booking in bookings:
                        booking.date = booking.date.strftime('%d-%m-%Y')
                    data_available = None if len(bookings) == 0 else 1
                    return render(request, 'confroom_app/booking.html',
                                  {'room': room, 'bookings': bookings, 'data_available': data_available, 'comment': comment})
            else:
                return HttpResponse("Date cannot be earlier than today")
        else:
            return HttpResponse(f"{room.name} already booked for {date}")
        return redirect('book-room', room_id)

class ShowRoom(View):
    def get(self, request, room_id):
        room_id = int(room_id)
        room = get_object_or_404(Room, pk=room_id)
        bookings = Booking.objects.filter(room=room, date__gte=date.today()).order_by('date')
        for booking in bookings:
            booking.date = booking.date.strftime("%d-%m-%Y")
        data_available = None if len(bookings) == 0 else 1
        return render(request, 'confroom_app/show_room.html', {'room': room, 'bookings': bookings, 'data_available': data_available})

class SearchRooms(View):
    def get(self, request):
        # name = request.GET.get('name', '').strip()
        # capacity = request.GET.get('capacity', '').strip()
        # has_projector = request.GET.get('has_projector','')
        all_rooms = Room.objects.all()
        if len(all_rooms) == 0:
            result = None
        else:
            result = 1
        return render(request, 'confroom_app/search.html', {'all_rooms': all_rooms, 'result': result})

    def post(self, request):
        name = (request.POST['name']).strip()
        capacity = request.POST['capacity']
        has_projector = request.POST.get('has_projector') == "on"
        all_rooms = Room.objects.all()
        if name:
            all_rooms = all_rooms.filter(name__icontains=name)
        if capacity.isdigit():
            all_rooms = all_rooms.filter(capacity__gte=int(capacity))
            capacity = int(capacity)
        if has_projector:
            all_rooms = all_rooms.filter(has_projector=True)
            projector = 1
        else:
            all_rooms = all_rooms.all()
            projector = None
        if len(all_rooms) == 0:
            result = None
        else:
            result = 1
        return render(request, 'confroom_app/search.html', {'all_rooms': all_rooms, 'result': result,
                                                            'projector': projector, 'capacity': capacity, 'name': name})
