from django.contrib import admin
from .models import Programs, Classes, Schedule,\
                    Trainer, Types, ContactUs


admin.site.register(Programs)
admin.site.register(Classes)
admin.site.register(Schedule)
admin.site.register(Trainer)
admin.site.register(Types)
admin.site.register(ContactUs)



# Register your models here.
