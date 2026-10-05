from django.shortcuts import render, redirect
from .models import Workout, WorkoutTemplate
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

    # request method GET renders a blank form
    else:
        form = WorkoutForm()
    return render(request, 'tracker/add_workout.html', {'form': form})

# view that asks how many days per week the user wants to train
def choose_days(request):
    return render(request, 'tracker/choose_days.html', {'options': range(2, 7)})

# view that lists the workout templates for the chosen number of days
def template_list(request, days):
    if not 2 <= days <= 6:
        return redirect('choose_days')
    templates = WorkoutTemplate.objects.filter(
        days_per_week=days
    ).prefetch_related('exercises')
    return render(
        request,
        'tracker/template_list.html',
        {'days': days, 'templates': templates},
    )