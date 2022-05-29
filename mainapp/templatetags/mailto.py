from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def mail_to(link):
    return mark_safe(f"<a href='mailto:{link}'>{link}</a>")
