from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from ninja import Router, Form, File, UploadedFile

from event.models import User
from event.models import Event
from event.schemas import EventOut, EventIn

router = Router()

@router.get("/event/{int:event_id}", response=EventOut)
def eventid(request, event_id):
    return get_object_or_404(Event, pk=event_id)

@router.get("/events", response=list[EventOut])
def events(request):
    return get_list_or_404(Event)


@router.post("/create_event")
def create_event(request, event: EventIn= Form(...)):
    n_event = Event(**event.dict())
    n_event.host = User.objects.get(username="admin")
    n_event.save()
    return JsonResponse({'id': n_event.id}, status=201)