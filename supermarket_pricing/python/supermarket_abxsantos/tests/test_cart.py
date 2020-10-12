import unittest

from src.cart import CartProduct
from src.product.products import Product


class TestCartProduct(unittest.TestCase):
    def test_remove_item_from_stock_must_remove_from_stock_when_cart_item_is_created(self):
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        cart_item = CartProduct(sweet_potato, 10)
        self.assertEqual(cart_item.quantity, 10)
        self.assertEqual(sweet_potato.stock_quantity, 90)

    def test_remove_item_from_stock_must_raise_error_when_not_enough_products_in_stock(self):
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=9, unit='Kg')
        with self.assertRaises(ValueError):
            CartProduct(sweet_potato, 10)
        self.assertEqual(sweet_potato.stock_quantity, 9)

    def test_increase_quantity_must_raise_error_when_not_enough_products_in_stock(self):
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=11, unit='Kg')
        cart_product = CartProduct(sweet_potato, 10)
        with self.assertRaises(ValueError):
            cart_product.increase_quantity(10)
        self.assertEqual(sweet_potato.stock_quantity, 1)

    def test_increase_quantity_must_add_products_removing_from_stock(self):
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=11, unit='Kg')
        cart_product = CartProduct(sweet_potato, 10)
        cart_product.increase_quantity(1)
        self.assertEqual(sweet_potato.stock_quantity, 0)

    def test_restore_item_to_stock_must_remove_products_adding_back_to_stock(self):
        sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=11, unit='Kg')
        cart_product = CartProduct(sweet_potato, 10)
        cart_product.restore_item_to_stock(5)
        self.assertEqual(sweet_potato.stock_quantity, 6)
