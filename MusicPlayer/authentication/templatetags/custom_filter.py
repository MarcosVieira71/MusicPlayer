from django import template

register = template.Library()

@register.filter(name='ms_to_minutes')
def ms_to_minutes(milliseconds):
    minutes = milliseconds // 60000
    seconds = (milliseconds % 60000) // 1000
    return f'{minutes}:{seconds:02d}'  # Formata como "minutos:segundos"
