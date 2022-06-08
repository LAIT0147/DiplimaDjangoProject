from django.shortcuts import render, redirect
from mainpage.models import ContactUs, Programs, Schedule
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def contactus_list(request):
    contact_lst = ContactUs.objects.filter(is_processed=False)
    return render(request, 'contactus_list.html', context={'contact_lst': contact_lst})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_contactus(request, pk):
    ContactUs.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:contactus_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def program_list(request):
    programs_list = Programs.objects.all
    return render(request, 'program_list.html', context={'programs_list': programs_list})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_program(request, pk):
    if Programs.objects.filter(pk=pk).filter(is_visible=True):
        Programs.objects.filter(pk=pk).update(is_visible=False)
    else:
        Programs.objects.filter(pk=pk).update(is_visible=True)
    return redirect('manager:program_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def schedule_list(request):
    schedule = Schedule.objects.all()
    return render(request, 'schedule_list.html', {'schedule': schedule})


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_schedule(request, pk):
    if Schedule.objects.filter(pk=pk).filter(is_visible=True):
        Schedule.objects.filter(pk=pk).update(is_visible=False)
    else:
        Schedule.objects.filter(pk=pk).update(is_visible=True)
    return redirect('manager:schedule_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def delete_training(request, pk):
    training = Schedule.objects.get(pk=pk)
    training.delete()
    return redirect('manager:schedule_list')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def edit_training(request, pk):
    week = Schedule.objects.get(pk=pk)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=week)
        if form.is_valid():
            form.save()
            return redirect('manager:schedule_list')
    else:
        form = ScheduleForm(instance=week)
    return render(request, 'edit_training.html', {'form': form})