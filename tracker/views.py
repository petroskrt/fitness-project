from django.shortcuts import render, redirect
from .models import Workout
from .forms import WorkoutForm

# Create your views here.

# view to list all the workouts
def workout_list(request):
    workouts = Workout.objects.all().order_by('-date')
    return render(request, 'tracker/workout_list.html', {'workouts': workouts})

# view to add a workout
def add_workout(request):
    
    # request method POST when user fills and submits form
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workout_list')
        
    # requst method GET renders a balnk form and renders it
    else:
        form = WorkoutForm()
    return render(request, 'tracker/add_workout.html', {'form': form})