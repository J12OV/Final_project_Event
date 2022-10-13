import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from event.models import Event, Participant, Category

#
# # Create your views here.
def hello(request, s):
     return HttpResponse(f'Hello, {s} world!')
#
#
def home(request):
    events = Event.objects.all()  # najdeme všechny místnosti

    context = {'events': events}
    return render(request, 'event/home.html', context)
#
#
@login_required
def search(request):
    if request.method == 'POST':  # pokud pošleme dotaz z formuláře
        s = request.POST.get('search')                       # z odeslané proměnné si vytáhnu, co chci hledat
        s = s.strip()                                        # ořízneme prázdné znaky
        if len(s) > 0:                                       # pkud s obsahuje alespoň jeden znak
            events = Event.objects.filter(name__contains=s)        # vyfiltruji události dle zadaného řetězce
            participants = Participant.objects.filter(body__contains=s)  # vyfiltruji uživatele dle zadaného řetezce

            context = {'events': events, 'participants': participants, 'search': s }     # výsledky uložím do kontextu
            return render(request, "event/search.html", context)  # vykreslíme stránku s výsledky
        return redirect('home')


    return redirect('home')

# # @login_required
# # def search(request, s):
# #         rooms = Room.objects.filter(name__contains=s)
# #         messages = Message.objects.filter(body__contains=s)
# #
# #         context = {'rooms': rooms, 'messages': messages}
# #     return render(request, "chatterbox/search.html", context)

@login_required
def event(request, pk):
    event = Event.objects.get(id=pk)
    user = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        participate = request.POST.get('participate')
        #participant = Participant.objects.get(user=request.user)
        try:
            event.participants.add(user)
           # participant = Participant.objects.create(
             #   user=request.user,
             #   event=event,
          #  )
        except:
            print("Participant is already signed up")
            context = {'event': event, 'error': "Participant is already signed"}
            return render(request, 'event/event.html', context)

    #participants = Participant.objects.filter(event=pk)  # vybereme všechny uživatele dané události
    context = {'event': event }
    return render(request, "event/event.html", context)

@login_required
def events(request):#filter_from, filter_to
    if request.method == 'POST':
        filter_from = request.POST.get('filter_from')
        filter_to = request.POST.get('filter_to')
        current_events = request.POST.get('current_events')
        current_events = Event.objects.filter(startdatetime__gte=filter_from)
        events = Event.objects.filter(startdatetime__gte=filter_from, enddatetime__lte=filter_to)
    else:
        events = Event.objects.all()

    #all = Event.objects.all()
    # filter_from= Event.objects.filter(startdatetime__gte=datetime.datetime.now())
    # filter_to = Event.objects.filter_to(startdatetime__gte=datetime.datetime.now())
    context = {'events': events}
    return render(request, "event/events.html", context)
#
#
@login_required
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        category_id = request.POST.get('category').strip()
        category = Category.objects.get(id=category_id)

        typeonline = False
        if request.POST.get('typeonline') == 'on':
            typeonline = True
        typefysical = False
        if request.POST.get('typefysical') == 'on':
            typefysical = True

        location = request.POST.get('location').strip()
        startdatetime = request.POST.get('startdatetime').strip()
        enddatetime = request.POST.get('startdatetime').strip()
        organizer = request.POST.get('organizer').strip()
        descr = request.POST.get('descr').strip()
        photo = request.POST.get('upload')
        try:
            if len(name) > 0:
                event = Event.objects.create(
                    host=request.user,
                    name=name,
                    category=category,
                    typeonline=typeonline,
                    typefysical=typefysical,
                    location=location,
                    startdatetime=startdatetime,
                    enddatetime=enddatetime,
                    descr=descr,
                )

                return redirect('event', pk=event.id)
        except:
            print("not filled completely formular")


    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'event/create_event.html', context)


@login_required
def delete_event(request, pk):
    event = Event.objects.get(id=pk)
    if event.participants_count() == 0:  # pokud v události není žádná uživatel
        event.delete()               # tak místnost smažeme
        return redirect('events')

    context = {'event': event, 'participants_count': event.participants_count()}
    return render(request, 'event/delete_event.html', context)

def delete_event_yes(request, pk):
    event = Event.objects.get(id=pk)
    event.delete()
    return redirect('events')


class EventEditForm(ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

#view
@method_decorator(login_required, name ='dispatch')
class EditEvent(UpdateView):
    template_name='event/edit_event.html'
    model = Event
    form_class = EventEditForm
    success_url = reverse_lazy('home')