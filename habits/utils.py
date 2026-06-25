import datetime

ANCHOR_DATE = datetime.date(2026, 1, 1)


def is_scheduled(habit, day):
    if habit.frequency_type == 'daily':
        return True
    if habit.frequency_type == 'every_n_days':
        delta = (day - ANCHOR_DATE).days
        return delta % habit.frequency_value == 0
    return True
