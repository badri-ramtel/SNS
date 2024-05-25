from django.shortcuts import render, redirect
from main_app.models import Slider, President, Subscribe, Adversite
from about_app.models import About
from gallery_app.models import Category, Photo
from event_app.models import Event, CreateEvent
from document_app.models import Laws, References, Appreciations
from itertools import chain
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    obj = Slider.objects.all()
    # counter = Slider.objects.all().count()
    # print('counter:', counter) 
    about = About.objects.all()
    pre = President.objects.all()
    categories = Category.objects.all()
    photos = Photo.objects.all()
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    laws = Laws.objects.all()
    ref = References.objects.all()
    app = Appreciations.objects.all()
    docs = list(chain(laws, ref, app))
    # docs = chain(laws, ref, app)
    # docs = Laws.objects.all() 
    adv = Adversite.objects.all()
    context = {'obj': obj, 'about': about, 'pre': pre, 'categories': categories, 'photos': photos, 'eventor': eventor, 'news': news, 'docs': docs, 'adv': adv}
    return render(request, 'main_app/home.html', context) 

def slider(request):
    slide = Slider.objects.all()
    context = {'slide': slide}
    return render(request, 'main_app/slider.html', context)

def president(request):
    president = President.objects.all()
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    context = {'president': president, 'eventor': eventor, 'news': news}
    return render(request, 'main_app/president.html', context)


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        form = Subscribe(email= email)
        form.save()
        messages.success(request, 'SNS Family Thank you for registering!!!')
        return redirect(request.META['HTTP_REFERER'])

    
# def ads(request):
#     adv = Adversite.objects.all()
#     context = {'adv': adv}
#     return render(request, 'main_app/home.html', context)