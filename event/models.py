
from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Participant(models.Model):
    #event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.TextField(null=True, blank=False)
    photo = models.TextField(null=True, blank=True)

    class Meta:
        pass
    #    ordering = ['user.last_name', 'user.first_name']  # descending order

    def __str__(self):
        return self.event.name

    def events_count(self):
         user_events = self.event_set.all()
         return user_events.count()
class Message(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    file = models.TextField(null=True)  # file attribute in model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']  # descending order

    def __str__(self):
        return self.body[0:50]


class Event(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)


    # TODO category = models.ForeignKey(Category, on_delete=models.SET_NULL, null)
    typeonline = models.BooleanField(null=True, blank=True)
    typefysical = models.BooleanField(null=True, blank=True)
    location = models.TextField(null=True,blank=True)
    startdatetime = models.DateTimeField(null=True, blank=True)
    enddatetime = models.DateTimeField(null= True, blank=True)
    organizer = models.TextField(null=True, blank=True)
    descr = models.TextField(null=True, blank=True)
    photo = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="evparticipants",  blank=True)
    # messages = models.ManyToManyField(Message, related_name="evmessages", blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['startdatetime', 'enddatetime']  # descending order

    def __str__(self):
        return self.name

    def last_message_time(self):
        event_message = self.message_set.all()[0]
        return event_message.updated


    def participants_count(self):
        #eventparticipants = self.participants.evparticipants_set.all()
        return self.participants.count()

    # def last_message_time(self):
    #     room_message = self.message_set.all()[0]
    #     return room_message.updated


class Message(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(null=False, blank=False)
    file = models.TextField(null=True)  # file attribute in model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created', '-updated']  # descending order

    def __str__(self):
        return self.body[0:50]











