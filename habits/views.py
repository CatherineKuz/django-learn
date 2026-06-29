import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog
from .utils import is_scheduled
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    today = datetime.date.today()
    days = [today - datetime.timedelta(days=i) for i in range(6, -1, -1)]
    habits = Habit.objects.filter(user=request.user)

    logs = HabitLog.objects.filter(habit__in=habits, date__in=days)
    log_set = {(log.habit_id, log.date) for log in logs}

    grid = [
        {
            'habit': habit,
            'cells': [
                {'date': day, 'done': (habit.id, day) in log_set, 'scheduled': is_scheduled(habit, day)}
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
        frequency_type = request.POST.get('frequency_type', 'daily')
        frequency_value = int(request.POST.get('frequency_value', 1))
        if name:
            Habit.objects.create(name=name, frequency_type=frequency_type, frequency_value=frequency_value, user=request.user)
    return redirect('dashboard')


@login_required
def habit_delete(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    habit.delete()
    return redirect('dashboard')


@login_required
def log_toggle(request, pk, date_str):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    day = datetime.date.fromisoformat(date_str)
    log, created = HabitLog.objects.get_or_create(habit=habit, date=day)
    if not created:
        log.delete()
    return redirect('dashboard')


@login_required
def habit_edit(request, pk):
    habit = get_object_or_404(Habit, pk=pk, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        frequency_type = request.POST.get('frequency_type', 'daily')
        frequency_value = int(request.POST.get('frequency_value', 1))
        if name:
            habit.name = name
            habit.frequency_type = frequency_type
            habit.frequency_value = frequency_value
            habit.save()
            return redirect('dashboard')
    return render(request, 'habits/habit_edit.html', {'habit': habit})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})