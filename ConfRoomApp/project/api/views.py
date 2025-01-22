from confroom_app.models import Booking, Room
from project.serializers import RoomSerializer, BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def room_list(request, format=None):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def booking_list(request, format=None):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
