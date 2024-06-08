from django.shortcuts import render, redirect
from contact_app.models import FeedBack, FeedbackInstruction, Member, MemberInstruction, Vacancy, VacancyInstruction, Donation, DonationInstruction
from event_app.models import Event, CreateEvent
from django.contrib import messages


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        feedback = request.POST.get('feedback')
        form = FeedBack(full_name= name, 
                        email= email, 
                        address= address, 
                        contact= contact, 
                        feedback= feedback
                        )
        form.save()
        messages.success(request, 'SNS canada Thank you for your Feedback!')
        return redirect('contactapp-contact')
    ins = FeedbackInstruction.objects.all()
    context = {'ins': ins}
    return render(request, 'contact_app/contact.html', context)


def member(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code = request.POST.get('pcode')
        membership = request.POST.get('membership')
        screenshot = request.FILES.get('screenshot')
        form = Member(  first_name= first_name, 
                        last_name= last_name, 
                        email= email, 
                        contact= contact, 
                        address1= address1, 
                        address2= address2,   
                        city= city,
                        province= province,
                        postal_code= postal_code,
                        membership = membership,
                        screenshot= screenshot,
                    )
        form.save()
        messages.success(request, 'Welcome to SNS Canada family')
        return redirect('contactapp-member')
    
    ins = MemberInstruction.objects.all()
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    context = {'ins': ins, 'eventor': eventor, 'news': news}
    return render(request, 'contact_app/member.html', context)

def vacancy(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    vacancies = Vacancy.objects.all()
    ins = VacancyInstruction.objects.all()
    context = {'vacancies': vacancies, 'eventor': eventor, 'news': news, 'ins': ins}
    return render(request, 'contact_app/vacancy.html', context)

def view_vacancy(request, pk):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    vac = Vacancy.objects.get(id= pk)
    context = {'vac': vac , 'eventor': eventor, 'news': news}
    return render(request, 'contact_app/view_vacancy.html', context)

def donate(request):
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('pcode')
        country = request.POST.get('country')
        donation_type = request.POST.get('donation_type')
        amount = request.POST.get('amount')
        screenshot = request.FILES.get('screenshot')
        form = Donation(first_name= first_name, 
                        last_name= last_name, 
                        email= email, 
                        contact= contact, 
                        address_1= address1, 
                        address_2= address2,   
                        city= city,
                        state= state,
                        postal_code= postal_code,
                        country= country,
                        donation_type = donation_type,
                        amount= amount,
                        screenshot= screenshot,
                        )
        form.save()
        messages.success(request, 'Your generosity will always be remember By SNS Family!!!')
        return redirect('contactapp-donate')
    
    ins = DonationInstruction.objects.all()
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    context = {'ins': ins, 'eventor': eventor, 'news': news}
    return render(request, 'contact_app/donate.html', context)