from django.contrib import admin
from .models import Workout, WorkoutTemplate, TemplateExercise
# Register your models here.

admin.site.register(Workout)
class TemplateExerciseInline(admin.TabularInline):
    model = TemplateExercise
    extra = 3
    
@admin.register(WorkoutTemplate)
class WorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = ("name", "days_per_week")
    inlines = [TemplateExerciseInline]