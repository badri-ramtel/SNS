from django.contrib import admin
from event_app.models import CreateEvent, Event

# Register your models here.
admin.site.register(CreateEvent)
admin.site.register(Event)