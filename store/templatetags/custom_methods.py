from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if str(product.id) in cart.keys():
        return True
    return False
