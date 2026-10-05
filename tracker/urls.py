from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_days, name = 'choose_days'),
    path('days/<int:days>/', views.template_list, name = 'template_list'),
    path('workouts/', views.workout_list, name = 'workout_list'),
    path('workouts/add/', views.add_workout, name = 'add_workout'),
]