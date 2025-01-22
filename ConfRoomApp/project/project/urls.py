from django.contrib import admin
from django.urls import path, include

from confroom_app.views import AddRoom, ModifyRoom, BookRoom, DeleteRoom, ShowRoom, Homepage, SearchRooms


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Homepage.as_view(), name="home"),
    path("room/new/", AddRoom.as_view(), name="add-room"),
    path("rooms/", SearchRooms.as_view(), name="search-rooms"),
    path("room/modify/<int:room_id>", ModifyRoom.as_view(), name="modify-room"),
    path("room/delete/<int:room_id>", DeleteRoom.as_view(), name="delete-room"),
    path("room/reserve/<int:room_id>", BookRoom.as_view(), name="book-room"),
    path("room/show/<int:room_id>", ShowRoom.as_view(), name="show-room"),
    path("api/", include("api.urls")),
]
