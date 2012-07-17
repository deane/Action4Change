#
# Custom filters for django templates
# add {% load 'custom_filters' %} to use
#

from django import template

register = template.Library()

def smart_truncate(content, length=50, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ''.join(content[:length]).strip() + suffix

def add_slashes(str):
    #add slashes when there is a quote
    return str.replace("'","\\'")

