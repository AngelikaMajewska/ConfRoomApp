from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    has_projector = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}, capacity: {str(self.capacity)}, projector: {str(self.has_projector)}"

class Booking(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.room}"

    class Meta:
        unique_together = (("date", "room"),)