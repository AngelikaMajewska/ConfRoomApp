from django.urls import path, re_path, include

from api.views import room_list, booking_list
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("bookings/", booking_list),
    path("rooms/", room_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)