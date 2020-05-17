from django.contrib import admin
from .models import Event, Routine, Task, Activity
# Register your models here.
admin.site.register(Event)
admin.site.register(Routine)
admin.site.register(Task)
admin.site.register(Activity)
