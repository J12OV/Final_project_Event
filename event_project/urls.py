"""event_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import event.views

from django.conf import settings  # add this
from django.conf.urls.static import static  # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', event.views.home, name='home'),


    # path(<cesta>, <view>, name=<name>)
    path('hello/<s>', event.views.hello),
    path('search/', event.views.search, name="search"),
    # path('search/<s>', chatterbox.views.search, name="search_s"),  # url patterns

    path('event/<str:pk>/', event.views.event, name='event'),  # {% url 'room'
    path('events/', event.views.events, name='events'),
    path('create_event/', event.views.create_event, name="create_event"),
    path('delete_event<pk>/', event.views.delete_event, name="delete_event"),
    # path('delete_room_yes/<pk>/', chatterbox.views.delete_room_yes, name="delete_room_yes"),
    path('edit_event/<pk>/', event.views.EditEvent.as_view(), name="edit_event"),
    # # path('create_room/new_room', chatterbox.views.new_room, name="create_room"),

    # accounts aplikace
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),  # login, logout,

]
