import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog


@login_required
def dashboard(request):
    today = datetime.date.today()
    days = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    habits = Habit.objects.all()

    logs = HabitLog.objects.filter(habit__in=habits, date__in=days)
    log_set = {(log.habit_id, log.date) for log in logs}

    grid = [
        {
            'habit': habit,
            'cells': [
                {'date': day, 'done': (habit.id, day) in log_set}
                for day in days
            ],
        }
        for habit in habits
    ]

    return render(request, 'habits/dashboard.html', {'days': days, 'grid': grid})


import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog


@login_required
def dashboard(request):
    today = datetime.date.today()
    days = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    habits = Habit.objects.all()

    logs = HabitLog.objects.filter(habit__in=habits, date__in=days)
    log_set = {(log.habit_id, log.date) for log in logs}

    grid = [
        {
            'habit': habit,
            'cells': [
                {'date': day, 'done': (habit.id, day) in log_set}
                for day in days
            ],
        }
        for habit in habits
    ]

    return render(request, 'habits/dashboard.html', {'days': days, 'grid': grid})


@login_required
def habit_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Habit.objects.create(name=name)
    return redirect('dashboard')


@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('dashboard')


@login_required
def log_toggle(request, pk, date_str):
    habit = get_object_or_404(Habit, pk=pk)
    day = datetime.date.fromisoformat(date_str)
    log, created = HabitLog.objects.get_or_create(habit=habit, date=day)
    if not created:
        log.delete()
    return redirect('dashboard')


def habit_add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        if name:
            Habit.objects.create(name=name)
    return redirect('dashboard')


@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    habit.delete()
    return redirect('dashboard')


@login_required
def log_toggle(request, pk, date_str):
    habit = get_object_or_404(Habit, pk=pk)
    day = datetime.date.fromisoformat(date_str)
    log, created = HabitLog.objects.get_or_create(habit=habit, date=day)
    if not created:
        log.delete()
    return redirect('dashboard')
