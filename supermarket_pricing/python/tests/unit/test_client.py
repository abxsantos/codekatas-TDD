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

    def test_add_product_to_cart_must_add_an_item_to_empty_client_cart(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        client.add_product_to_cart(sweet_potato, 1)
        self.assertEqual(len(client.cart), 1)
        self.assertEqual(client.cart.pop().product, sweet_potato)

    def test_add_product_to_cart_must_increase_an_cart_product_quantity_if_it_exists_in_cart(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        client.add_product_to_cart(sweet_potato, 1)
        client.add_product_to_cart(sweet_potato, 2)
        self.assertEqual(len(client.cart), 1)
        self.assertEqual(client.cart.pop().quantity, 3)

    def test_add_product_to_cart_must_raise_exception_when_not_enough_product_in_stock(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        with self.assertRaises(ValueError):
            client.add_product_to_cart(sweet_potato, 101)

    def test_add_product_to_cart_must_raise_exception_when_adding_more_than_product_in_stock(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        client.add_product_to_cart(sweet_potato, 100)
        with self.assertRaises(ValueError):
            client.add_product_to_cart(sweet_potato, 1)

    def test_remove_product_from_cart_must_remove_an_item_from_client_cart(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        client.add_product_to_cart(sweet_potato, 1)
        client.remove_product_from_cart(sweet_potato, 1)
        empty_cart = set()
        self.assertEqual(client.cart, empty_cart)
        self.assertEqual(sweet_potato.stock_quantity, 100)

    def test_remove_product_from_cart_must_remove_a_specified_quantity_from_client_cart(self):
        client = Client('Wilson')
        sweet_potato = Product(name='sweet potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        client.add_product_to_cart(sweet_potato, 2)
        client.remove_product_from_cart(sweet_potato, 1)
        self.assertEqual(client.cart.pop().quantity, 1)
        self.assertEqual(sweet_potato.stock_quantity, 99)

    def test_calculate_cart_price_must_return_the_correct_value(self):
        wilson = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        wilson.add_product_to_cart(sweet_potato, 3)
        self.assertEqual(wilson._calculate_cart_price(), 3.00)

    def test_calculate_cart_price_must_return_0_when_no_items_in_cart(self):
        wilson = Client('Wilson')
        self.assertEqual(wilson._calculate_cart_price(), 0.00)

    def test_pay_must_raise_exception_if_client_has_no_money(self):
        wilson = Client('Wilson')
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        wilson.add_product_to_cart(sweet_potato, 100)
        with self.assertRaises(Exception):
            wilson.pay()
    #
    # def test_pay_must_remove_correct_quantity_from_user_wallet(self):
    #     wilson = Client(name='Wilson', wallet=10.00)
    #     sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
    #     cart_sweet_potato = CartProduct(product=sweet_potato, quantity=3)
    #     wilson.add_product_to_cart(cart_sweet_potato)
    #     wilson.pay()
    #     self.assertEqual(wilson.wallet, 7.00)