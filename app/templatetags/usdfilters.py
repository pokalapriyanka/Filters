from django import template
register=template.Library()


def swap(value):
    return value.swapcase()

#@register.filter()
@register.filter(name='remove')
def remove(value,char):
    return value.replace(char,'')

register.filter('swapcase',swap)
#register.filter('rem',remove)