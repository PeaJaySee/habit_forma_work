from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Habit(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, default="None")
    description = models.CharField(max_length=100, default="enter description here")
    frequency = models.CharField(max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    def mark_complete(self):
        today = date.today()
        if not Progress.objects.filter(habit=self, date=today).exists():
            self.is_complete = True
            self.completion_date = today
            self.save()
            Progress.objects.create(habit=self, date=today, status=True)

class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
    
    class Meta:
        verbose_name_plural = "Progress"
       # unique_together = ('habit', 'date')