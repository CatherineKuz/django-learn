from django.db import models


class Habit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()

    class Meta:
        unique_together = [('habit', 'date')]

    def __str__(self):
        return f'{self.habit.name} — {self.date}'

