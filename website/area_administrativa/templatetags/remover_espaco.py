from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='trim')
@stringfilter
def trim(value):
    """
    Remove espaços em branco do início e do fim de uma string.
    """
    return value.strip()