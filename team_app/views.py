from django.shortcuts import render, redirect
from team_app.models import Year_Book, Committee, SubMenu
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def team(request):
    teams = request.GET.get('member')
    if teams == None:
        community = Committee.objects.filter(year__current_year= True)
        # community = Committee.objects.all()
    else:
        community = Committee.objects.filter(year__year_frame= teams)
        
    committee = Year_Book.objects.all() 
    paginator = Paginator(community,12)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)

    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    quote = SubMenu.objects.all()
    context = {'page_obj': page_obj, 'committee': committee, 'quote': quote}
    return render(request, 'team_app/committee.html', context) 

def viewCommittee(request, pk): 
    community = Committee.objects.get(id= pk)
    committee = Year_Book.objects.all() 
    context = {'community': community, 'committee': committee}
    return render(request, 'team_app/viewcommittee.html', context)
