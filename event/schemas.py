from ninja import ModelSchema
from event.models import Event

class EventOut(ModelSchema):
    class Config:
        model = Event
        model_fields = ["name","category", "descr", "startdatetime","enddatetime","typeonline","typefysical","organizer"]

class EventIn(ModelSchema):
    class Config:
        model = Event
        model_fields = ["name","category", "descr", "startdatetime","enddatetime","typeonline","typefysical","organizer"]
