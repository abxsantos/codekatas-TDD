import unittest

from cart.cart import CartProduct
from client.client import Client
from product.products import Product


class TestClient(unittest.TestCase):
    def test_client_must_have_a_name(self):
        client = Client('Wilson')
        self.assertEqual(client.name, 'Wilson')

    def test_client_must_be_initialized_with_an_empty_cart(self):
        client = Client('Wilson')
        empty_cart = set()
        self.assertEqual(client.cart, empty_cart)

    def test_add_product_to_cart_must_add_an_item_to_client_cart(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_sweet_potato = CartProduct(product=sweet_potato, quantity=1)
        client.add_product_to_cart(cart_sweet_potato, 1)
        self.assertEqual(client.cart, {cart_sweet_potato})
        self.assertEqual(sweet_potato.stock_quantity, 99)

    def test_remove_product_from_cart_must_remove_an_item_from_client_cart(self):
        wilson = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_sweet_potato = CartProduct(product=sweet_potato, quantity=1)
        wilson.add_product_to_cart(cart_sweet_potato, 1)
        wilson.remove_product_from_cart(cart_sweet_potato, 1)
        empty_cart = set()
        self.assertEqual(wilson.cart, empty_cart)
        self.assertEqual(sweet_potato.stock_quantity, 100)

    def test_calculate_cart_price_must_return_the_correct_value(self):
        wilson = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_sweet_potato = CartProduct(product=sweet_potato, quantity=3)
        wilson.add_product_to_cart(cart_sweet_potato)
        self.assertEqual(wilson._calculate_cart_price(), 3.00)

    def test_pay_must_raise_exception_if_client_has_no_money(self):
        wilson = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_sweet_potato = CartProduct(product=sweet_potato, quantity=3)
        wilson.add_product_to_cart(cart_sweet_potato)
        with self.assertRaises(Exception):
            wilson.pay()

    def test_pay_must_remove_correct_quantity_from_user_wallet(self):
        wilson = Client(name='Wilson', wallet=10.00)
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_sweet_potato = CartProduct(product=sweet_potato, quantity=3)
        wilson.add_product_to_cart(cart_sweet_potato)
        wilson.pay()
        self.assertEqual(wilson.wallet, 7.00)