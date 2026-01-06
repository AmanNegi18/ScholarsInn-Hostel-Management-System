from django.db import models
from django.contrib.auth.models import User


class Hostel(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.hostel.name} - Room {self.room_number}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll = models.PositiveIntegerField(unique=True)
    phone = models.CharField(max_length=15)
    parent_phone = models.CharField(max_length=15)
    room = models.ForeignKey(Room, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username} ({self.roll})"


class MessMenu(models.Model):
    day = models.CharField(max_length=20)
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return self.day


class Notice(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
