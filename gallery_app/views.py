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
        photos = Photo.objects.filter(category__name= cat) 

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


def viewPhoto(request, pk):
    categories = Category.objects.all()
    photo = Photo.objects.get(id= pk)
    committee = Year_Book.objects.all()
    context = {'categories': categories, 'photo': photo, 'committee': committee}
    return render(request, 'gallery_app/viewphoto.html', context)
