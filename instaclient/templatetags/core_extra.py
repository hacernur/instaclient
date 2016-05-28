#-*- coding: utf-8 -*-

from django import template
from django.forms.extras import widgets


register = template.Library()


@register.simple_tag
def add_attrs(field, **kwargs):
    attr_names = kwargs.keys()

    for attr_name in attr_names:

        field.field.widget.attrs.update({
            attr_name.replace("_", "-"):kwargs[attr_name]
            })

    return field

@register.filter
def lower(text):
    return text.lower()

@register.filter
def upper(text):
    return text.upper()

@register.filter
def splitUrl(url, index=-1):
    url_list = url.split('/')

    try:
        return url_list[index]
    except IndexError:
        return url_list[-1:] if url_list[-1:] != [] else ''

@register.filter
def percent_number(number1, number2):
    percent = 0
    try:
        percent = number1 * 100 / number2
    except ZeroDivisionError:
        percent = 0

    return "%.1f" %(percent)

@register.filter
def percent_list(list1, list2):
    percent = 0
    try:
        percent = len(list1) * 100 / len(list2)
    except ZeroDivisionError:
        percent = 0

    return "%.1f" %(percent)

@register.filter
def size_humanize(size):
    for unit in ['B','KB','MB','GB','TB','PB','EB','ZB']:
        if abs(size) < 1024.0:
            return "%3.2f%s" % (size, unit)

        size /= 1024.0
    return "%.2f%s%s" % (size, 'Y')
