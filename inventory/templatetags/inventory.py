from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="get_url")
@stringfilter
def get_filtered_url(value, arg):
    if '?' in value:
        # Already has a queryset
        if '&order' in value:
            # Only one order for query
            # Remove last order from url
            new_url = value[0:value.find('&order')]
            return "{}&order={}".format(new_url, arg)
        return "{}&order={}".format(value, arg)
    else:
        return "{}?order={}".format(value, arg)


@register.filter(name="get_page")
@stringfilter
def get_page_url(value, arg):
    if '?' in value:
        # Already has a queryset
        if '?page' in value:
            # Only one order for query
            # Remove last order from url
            old_page = (value[value.find('?page=')+6])
            new_url = value.replace(str(old_page), str(arg))
            return new_url
        else:
            pages_first = value[0:value.find('?')]
            filtering = value[value.find('?')+1:]
            return "{}?page={}&{}".format(pages_first, arg, filtering)
    else:
        return "{}?page={}".format(value, arg)
