from django.db import models

# Create your models here.
class Workout(models.Model):
    activity = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()

    def __str__(self):
        return f"{self.activity} - {self.duration} min on {self.date}"


class WorkoutTemplate(models.Model):
    name = models.CharField(max_length=100)
    days_per_week = models.PositiveSmallIntegerField(
        choices=[(i, f"{i} days") for i in range(2, 7)]
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.days_per_week} days)"


class TemplateExercise(models.Model):
    template = models.ForeignKey(
        WorkoutTemplate, related_name="exercises", on_delete=models.CASCADE
    )
    day_number = models.PositiveSmallIntegerField(default=1)
    day_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=100)
    sets = models.PositiveSmallIntegerField(default=3)
    reps = models.CharField(max_length=20, default="8-12")

    class Meta:
        ordering = ["day_number", "id"]

    def __str__(self):
        return self.name