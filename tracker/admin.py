from django.contrib import admin
from .models import Habit, Progress

#register models here
admin.site.register(Habit)
admin.site.register(Progress)
