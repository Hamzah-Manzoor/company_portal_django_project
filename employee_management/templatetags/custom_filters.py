from django import template
from datetime import datetime, timedelta

register = template.Library()


@register.filter
def subtract(value, arg):
    return value - arg


@register.filter
def format_lunch_time(lunch_time):
    start_time = datetime.strptime(str(lunch_time), '%H:%M:%S')
    end_time = (start_time + timedelta(hours=1)).time()
    formatted_start_time = start_time.strftime('%I:%M %p')
    formatted_end_time = end_time.strftime('%I:%M %p')
    return f"{formatted_start_time} - {formatted_end_time}"
