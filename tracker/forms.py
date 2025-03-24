from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency']
        widgets = {'description': forms.TextInput(attrs={'required': False}),
                   }

class HabitCompleteForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['is_complete']