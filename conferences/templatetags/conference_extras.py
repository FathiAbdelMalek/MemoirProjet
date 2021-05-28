from django import template

register = template.Library()


@register.simple_tag
def get_url(field_name, value, urlencode=None):
    url = "?{}={}".format(field_name, value)
    if urlencode:
        query = urlencode.split('&')
        filtered = filter(lambda p: p.split('=')[0] != field_name, query)
        encoded = '&'.join(filtered)
        url = '{}&{}'.format(url, encoded)
    return url
