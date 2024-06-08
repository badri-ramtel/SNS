from django.shortcuts import render, redirect
from main_app.models import Slider, President, Subscribe, Advertisement
from about_app.models import About
from gallery_app.models import Category, Photo
from event_app.models import Event, CreateEvent
from document_app.models import Laws, References, Appreciations
from itertools import chain
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    slide = Slider.objects.all()
    count = Slider.objects.all().count()
    counter = range(count)
    about = About.objects.all()
    pre = President.objects.all()
    categories = Category.objects.all()
    photos = Photo.objects.all()
    cat = request.GET.get('category')
    if cat == None:
        photos = Photo.objects.all() 
    else:
        photos = Photo.objects.filter(category__name= cat) 
 
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    laws = Laws.objects.all()
    ref = References.objects.all()
    app = Appreciations.objects.all()
    docs = chain(laws, ref, app)
    adv = request.GET.get('advertise')
    if adv == None:
        ads = Advertisement.objects.all() 
    else:
        ads = Advertisement.objects.filter(content__id= adv)  
    context = {'slide': slide, 'counter': counter, 'about': about, 'pre': pre, 'categories': categories, 'photos': photos, 'eventor': eventor, 'news': news, 'docs': docs, 'ads': ads}
    return render(request, 'main_app/home.html', context) 


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

    
def advertise(request, pk):
    adv = Advertisement.objects.get(id= pk)
    context = {'adv': adv}
    return render(request, 'main_app/advertise.html', context)