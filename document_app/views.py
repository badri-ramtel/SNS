from django.shortcuts import render, redirect
from event_app.models import Event, CreateEvent
from document_app.models import Laws, References, Appreciations, Registrations, Program_Registrations
from django.contrib import messages

# Create your views here.
def lac(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    docs = Laws.objects.all()
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/lac.html', context)


def reference(request):
    # pre = President.objects.all()
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    docs = References.objects.all()
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/reference.html', context)

def appreciation(request):
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    docs = Appreciations.objects.all()
    context = {'eventor': eventor, 'docs': docs, 'news': news}
    return render(request, 'document_app/appreciation.html', context)

def register(request):
    if request.method == 'POST':
        your_name = request.POST.get('yname')
        age = request.POST.get('age')
        address = request.POST.get('address')
        city = request.POST.get('city')
        province = request.POST.get('province')
        postal_code = request.POST.get('pcode')
        your_contact = request.POST.get('ycontact')
        your_email = request.POST.get('yemail')
        parents_name = request.POST.get('pname')
        parents_contact = request.POST.get('pcontact')
        parents_email = request.POST.get('pemail')
        program = request.POST.get('program')
        screenshot = request.FILES.get('screenshot')
        form = Program_Registrations(
            participant_full_name= your_name, 
            age= age, 
            address= address, 
            city= city, 
            province= province, 
            postal_code= postal_code,   
            your_contact= your_contact,
            your_email= your_email,
            parents_full_name= parents_name,
            parents_contact= parents_contact,
            parents_email = parents_email,
            program = program,
            screenshot= screenshot,
            )
        form.save()
        messages.success(request, 'SNS Family Thank you for registering!!!')
        return redirect('documentapp-register')
    
    eventor = CreateEvent.objects.all()
    news = Event.objects.filter(created_events__event_name= 'News')
    reg = Registrations.objects.all()
    context = {'eventor': eventor, 'news': news, 'reg': reg}
    return render(request, 'document_app/program_registration.html', context)