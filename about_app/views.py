from django.shortcuts import render
from about_app.models import About, Vision, Term
from main_app.models import President
from event_app.models import Event, CreateEvent

# Create your views here.
def aboutUs(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    pre = President.objects.all()
    abo = About.objects.all()
    context = {'abo': abo, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/about.html', context)

def vision(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    pre = President.objects.all()
    vis = Vision.objects.all()
    context = {'vis': vis, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/vision.html', context)

def terms(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News') 
    pre = President.objects.all()
    ter = Term.objects.all()
    context = {'ter': ter, 'pre': pre, 'eventor': eventor, 'news': news}
    return render(request, 'about_app/terms.html', context)