from django.conf import settings
from django.db import models


class Habit(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Каждый день'),
        ('every_n_days', 'Каждые N дней'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=200)
    frequency_type = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='daily')
    frequency_value = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()

    class Meta:
        unique_together = [('habit', 'date')]

    def __str__(self):
        return f'{self.habit.name} — {self.date}'
