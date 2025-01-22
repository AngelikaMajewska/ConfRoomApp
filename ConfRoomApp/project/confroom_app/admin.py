
from django.contrib import admin

# Register your models here.
from confroom_app.models import Room, Booking

# dodaj te kategorie w panelu admina
admin.site.register(Room)
admin.site.register(Booking)