from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'required': True}), required=True)

    class Meta:
        model = Habit
        fields = ['description', 'frequency']
        widgets = {
            'description': forms.TextInput(attrs={'required': True}),
        }

class HabitCompleteForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['is_complete']