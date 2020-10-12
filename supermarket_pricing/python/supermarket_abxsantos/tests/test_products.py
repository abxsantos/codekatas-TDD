import unittest
from datetime import datetime

from src.product import ProductBundleDiscount
from src.product.products import Product

param_name_sku_list = [(1), ([]), (''), ({})]
param_cost_price_list = [("abc"), ([]), (''), ({})]


class TestProduct(unittest.TestCase):
    def test_product_must_raise_error_when_instantiated_with_no_properties(self):
        with self.assertRaises(TypeError):
            Product()

    def test_product_must_raise_error_when_instantiated_with_no_name(self):
        with self.assertRaises(TypeError):
            Product(name=None, cost=0.50, price=1.00, sku='001', unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_no_price(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=0.50, price=None, sku='001', unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_no_cost(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=None, price=1.00, sku='001', unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_no_sku(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=0.50, price=1.00, sku=None, unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_sku_that_is_not_a_string(self):
        for param_sku in param_name_sku_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=0.50, price=1.00, sku=param_sku, unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_name_that_is_not_a_string(self):
        for param_name in param_name_sku_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name=param_name, cost=0.50, price=1.00, sku='123', unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_cost_that_is_not_a_number(self):
        for param_cost in param_cost_price_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=param_cost, price=1.00, sku='123', unit='un', stock_quantity=100)

    def test_product_must_raise_error_when_instantiated_with_price_that_is_not_a_number(self):
        for param_price in param_cost_price_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=0.50, price=param_price, sku='123', unit='un', stock_quantity=100)

    def test_product_must_be_instantiated_given_correct_properties(self):
        product = Product(name='beans', cost=0.50, price=1.00, sku='001', unit='un', stock_quantity=100)
        self.assertEqual(product.name, 'beans')
        self.assertEqual(product.cost, 0.50)
        self.assertEqual(product.price, 1.00)
        self.assertEqual(product.sku, '001')

    def test_product_must_start_with_an_empty_price_history(self):
        product = Product(name='beans', cost=0.50, price=1.00, sku='001', unit='un', stock_quantity=100)
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(product.price_history)
        self.assertEqual(product.price_history, [(1.00, now)])

    def test_product_string_method_must_return_the_name(self):
        product = Product(name='beans', cost=0.50, price=1.00, sku='001', unit='un', stock_quantity=100)
        self.assertEqual(str(product), 'beans')

    def test_product_can_be_associated_with_a_bundle_discount(self):
        bundle_discount = ProductBundleDiscount(bundle_quantity=2, bundle_price=0.50)
        product = Product(name='beans', cost=0.50, price=1.00, sku='001', unit='un',
                          stock_quantity=100, bundle_discount=bundle_discount)
        self.assertEqual(product.bundle_discount.bundle_quantity, 2)
        self.assertEqual(product.bundle_discount.bundle_price, 0.50)
