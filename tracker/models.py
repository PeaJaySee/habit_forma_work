from django.db import models
from django.contrib.auth.models import User

class Habit(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    frequency = models.CharField(max_length=20, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly')])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Progress(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
