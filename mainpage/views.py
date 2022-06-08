from django.shortcuts import render, redirect
from .models import Programs, Classes, Schedule,\
                    Trainer, Types
from .forms import ContactUsForm


def main_page(request):
    if request.method == 'POST':
        contactus = ContactUsForm(request.POST)
        if contactus.is_valid():
            contactus.save()
            return redirect('/')

    contactus = ContactUsForm()
    programs = Programs.objects.order_by('position')
    classes = Classes.objects.order_by('position')
    schedule = Schedule.objects.order_by('position')
    trainer = Trainer.objects.order_by('name')
    expert = Trainer.objects.filter(is_visible=True, expert=True).order_by('name')
    types = Types.objects.order_by('position')

    return render(request, 'mainpage.html', context={'programs': programs, 'classes': classes,
                                                     'schedule': schedule, 'expert': expert,
                                                     'trainer': trainer, 'types': types,
                                                     'contactus': contactus,})
