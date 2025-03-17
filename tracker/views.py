from django.shortcuts import render
from django.views import generic
from .models import Habit
# Create your views here.

class HabitList(generic.ListView):
    model = Habit