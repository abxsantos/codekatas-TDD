import unittest

from supermarket_pricing.products import Product
from supermarket_pricing.supermarket import Supermarket


class ProductInserter(object):
    def __init__(self, supermarket: Supermarket, products: [Product]):
        """
        Used to insert products into the supermarket.
        Concerned with adding a new product to the supermarket.
        >>> bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001')
        >>> myrket_supermarket = Supermarket('mYrket')
        >>> ProductInserter(supermarket=myrket_supermarket, products=[bean_product]).add_products()
        >>> myrket_supermarket.products[0].name = 'beans'
        """
        self.products = products
        self.supermarket = supermarket

    def add_products(self) -> Supermarket:
        for product in self.products:
            self.supermarket.products.append(product)
        return self.supermarket


class TestProductInserter(unittest.TestCase):
    def test_batch_add_product_must_insert_a_product_into_supermaket_products_list(self):
        bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket, products=[bean_product]).add_products()
        self.assertEqual(len(myrket_supermarket.products), 1)

    def test_batch_add_product_must_insert_a_list_of_products_into_supermaket_products_list(self):
        bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001')
        rice_product = Product(name='rice', cost=0.50, price=1.00, sku='002')
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket, products=[bean_product, rice_product, sweet_potato_product]).add_products()
        self.assertEqual(len(myrket_supermarket.products), 3)

    def test_add_product_must_raise_typeerror_if_no_products_are_given(self):
        myrket_supermarket = Supermarket('mYrket')
        with self.assertRaises(TypeError):
            ProductInserter(supermarket=myrket_supermarket, products=None).add_products()
