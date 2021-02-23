from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    if str(product.id) in cart.keys():
        return True
    return False


@register.filter(name='cart_qty')
def cart_qty(product, cart):
    if str(product.id) in cart.keys():
        return cart.get(str(product.id))
    return 0


# calculate price for particular Product
@register.filter(name='total_price')
def total_price(product, cart):
    return product.price * cart_qty(product, cart)


# calculate price for total product in cart
@register.filter(name='total')
def total(products, cart):
    _sum = 0
    print('called')
    for p in products:
        _sum += total_price(p, cart)
    return _sum
