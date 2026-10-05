from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    def __str__(self): return self.number

class Student(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self): return self.name