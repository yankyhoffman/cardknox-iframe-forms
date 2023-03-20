from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def ifields_version():
    return '2.15.2302.0801'


@register.simple_tag
def ifields_key():
    return settings.CK_IFIELDS_KEY
