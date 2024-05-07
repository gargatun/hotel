from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def change_params(context, **params):
    query = context['request'].GET.copy()
    for key, value in params.items():
        if value is not None:
            query[key] = value
        elif key in query:
            del query[key]
    return query.urlencode()