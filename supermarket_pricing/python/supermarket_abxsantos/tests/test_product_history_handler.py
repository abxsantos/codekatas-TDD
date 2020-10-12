import unittest
from datetime import datetime

from src.product import ProductHistoryHandler
from src.product.products import Product


class TestProductHistoryHandler(unittest.TestCase):
    def test_change_price_must_add_the_new_price_and_datetime_of_the_change(self):
        sweet_potato_product = Product(name='beans', cost=0.50, price=1.00, sku='003', stock_quantity=100, unit='Kg')
        ProductHistoryHandler(product=sweet_potato_product, updated_price=1.25).change_product_price()
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.assertEqual(sweet_potato_product.price, 1.25)
        self.assertEqual(sweet_potato_product.price_history, [(1.00, now), (1.25, now)])

    def test_change_price_must_raise_warning_if_no_product_was_provided(self):
        with self.assertRaises(TypeError):
            ProductHistoryHandler(product=None, updated_price=1.25).change_product_price()

    def test_change_price_must_raise_warning_if_no_updated_price_was_provided(self):
        with self.assertRaises(TypeError):
            ProductHistoryHandler(product=None, updated_price=1.25).change_product_price()