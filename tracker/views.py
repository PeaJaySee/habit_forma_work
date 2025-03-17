from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from .forms import HabitForm
from .models import Habit
# Create your views here.


class HabitListView(LoginRequiredMixin, ListView, FormView):
    model = Habit
    template_name = 'tracker/habit_list.html'
    context_object_name = 'habit_list'
    form_class = HabitForm
    success_url = reverse_lazy('home')
    login_url = 'login'  # Redirect to login page if not authenticated

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def form_valid(self, form):
        habit = form.save(commit=False)
        habit.user = self.request.user
        habit.save()
        return super().form_valid(form)