from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm): # automatically generates form fields based on the Workout model
    
    class Meta:
        model = Workout
        fields = ['activity', 'duration', 'date']
        
        # widgets -> tells django to render the date field as an HTML date picker 
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }