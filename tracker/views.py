from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, FormView, UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = timezone.now().date()
        return context

    def form_valid(self, form):
        habit = form.save(commit=False)
        habit.user = self.request.user
        habit.save()
        return super().form_valid(form)
    
    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit = get_object_or_404(Habit, id=habit_id, user=request.user)
            habit.delete()
            return redirect('home')
        
        elif 'complete' in request.POST:
            habit_id = request.POST.get('habit_id')
            habit = get_object_or_404(Habit, id=habit_id, user=request.user)
            habit.mark_complete()
            return redirect('home')
        
        else:
            return super().post(request, *args, **kwargs)
        
class HabitUpdateView(LoginRequiredMixin, UpdateView):
    model = Habit
    form_class = HabitForm
    template_name = 'tracker/habit_update.html'
    success_url = reverse_lazy('home')
    login_url = 'login'  # Redirect to login page if not authenticated

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)