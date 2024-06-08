from django.shortcuts import render, redirect
from .models import Category, Photo
from team_app.models import Year_Book
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def gallery(request):
    cat = request.GET.get('category')
    if cat == None:
        photos = Photo.objects.all() 
    else:
        photos = Photo.objects.filter(category__id= cat) 
 
    categories = Category.objects.all()
    committee = Year_Book.objects.all()
    paginator = Paginator(photos,12)
    page_number = request.GET.get('page')
    try: 
        page_obj = paginator.get_page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {'categories': categories, 'committee': committee, 'page_obj': page_obj}
    return render(request, 'gallery_app/gallery.html', context)   

def grid(request, pk):
    categories = Category.objects.get(id= pk)
    context = {'categories': categories}


def viewPhoto(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id= pk)
    photo_ids = list(Photo.objects.values_list('id', flat= True))
    current_index= photo_ids.index(int(pk))
    try:
        next = photo_ids[current_index + 1]
        prev = photo_ids[current_index - 1]
    except IndexError:
        next = photo_ids[0]
        prev = photo_ids[int(len(photo_ids)) - 2]
        
    committee = Year_Book.objects.all()
    context = {'categories': categories, 'photo': photo, 'committee': committee, 'next': next, 'prev': prev}
    return render(request, 'gallery_app/viewphoto.html', context) 
