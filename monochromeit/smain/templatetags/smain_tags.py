from django import template


register = template.Library()

@register.inclusion_tag('smain/header.html')
def header():
    return {}

@register.inclusion_tag('smain/footer.html')
def footer():
    return {}
