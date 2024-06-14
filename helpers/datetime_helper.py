import calendar
from datetime import datetime


def get_day_of_week(date: datetime):
    return calendar.day_name[date.weekday()].capitalize()


def get_month_name_full(month: int):
    return calendar.month_name[month].capitalize()


def get_date_suffix(day: int):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    return suffix
