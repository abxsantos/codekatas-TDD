import unittest

from cart.cart import CartProduct
from product.products import Product


class Client(object):
    def __init__(self, name, wallet=None):
        """
        Supermarket client
        >>> wilson = Client(name='Wilson', wallet=10.00)
        >>> sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        >>> cart_sweet_potato = CartProduct(product=sweet_potato, quantity=1)
        >>> wilson.add_product_to_cart(cart_sweet_potato, 1)
        >>> wilson.pay()
        """
        self.name: str = name
        self.cart: set = set()
        self.wallet: float = wallet

    # TODO: Refactor this to accept product name as parameter, search into supermarket, create the cart product and add to cart
    def add_product_to_cart(self, cart_product: CartProduct, added_quantity=None):
        """Adds a given product to client cart"""
        if cart_product in self.cart and added_quantity:
            cart_product.increase_quantity(added_quantity)
        self.cart.add(cart_product)

    # TODO: Refactor this to accept product name as parameter, search into supermarket, remove the cart product and add to stock
    def remove_product_from_cart(self, cart_product: CartProduct, removed_quantity: int):
        """Removes a cart product from cart restoring it's quantity in stock"""
        cart_product.restore_item_to_stock(removed_quantity)
        self.cart.remove(cart_product)

    def _calculate_cart_price(self) -> float:
        """Calculates the cart total value"""
        total_price = 0
        for cart_product in self.cart:
            total_price += (cart_product.product.price * cart_product.quantity)
        return total_price

    # TODO: Refactor this to handle logic of bundle discount products
    def pay(self):
        """
        Pays for the cart total value
        :raises Exception: When the client has no money
        """
        total_price = self._calculate_cart_price()
        if total_price > self.wallet:
            raise Exception('Not enough money in the wallet!')
        self.wallet -= total_price



