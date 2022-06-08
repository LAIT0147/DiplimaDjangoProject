from django.urls import path
from manager.views import contactus_list, update_contactus,\
                        program_list, update_program,\
                        schedule_list, update_schedule, delete_training, edit_training


app_name = 'manager'

urlpatterns = [
    path('contactus/', contactus_list, name='contactus_list'),
    path('contactus/update/<int:pk>/', update_contactus, name='update_contactus'),
    path('programs/', program_list, name='program_list'),
    path('programs/update/<int:pk>/', update_program, name='update_program'),
    path('schedule/', schedule_list, name='schedule_list'),
    path('schedule/update_schedule/<int:pk>/', update_schedule, name='update_schedule'),
    path('schedule/delete/<int:pk>/', delete_training, name='delete_training'),
    path('schedule/edit_training/<int:pk>/', edit_training, name='edit_training'),
]