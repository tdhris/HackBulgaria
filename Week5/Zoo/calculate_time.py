def period_to_days(interval_of_time, period):
    if interval_of_time == 'days':
        return int(period)
    elif interval_of_time == 'months':
        return int(period) * 30
    elif interval_of_time == 'years':
        return int(period) * 365
    else:
        print("There's such period, you dummie!!!")
        return 0


def days_to_period(days, interval_of_time):
    if interval_of_time == 'months':
        return days / 30
    if interval_of_time == 'years':
        return days / 365
