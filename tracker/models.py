from django.db import models

# Create your models here.
class Workout(models.Model):
    activity = models.CharField(max_length=200)
    duration = models.IntegerField(help_text="Duration in minutes")
    date = models.DateField()
    
    def __str__(self):
        return f"{self.activity} - {self.duration} min on {self.date}"