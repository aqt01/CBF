from django import template


def get_element_name(element):
    return str(element._meta.verbose_name_plural)


register = template.Library()
register.filter('get_element_name', get_element_name)
