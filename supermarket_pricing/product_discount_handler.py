import unittest

from supermarket_pricing.product_inserter import ProductInserter
from supermarket_pricing.products import Product
from supermarket_pricing.supermarket import Supermarket


class ProductDiscountHandler(object):
    def __init__(self):
        """
        Concerned with creating discounts.
        """
        pass


class TestProductDiscountHandler(unittest.TestCase):
    def test_create_discount_must_change_the_quantity_of_product(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductDiscountHandler(myrket_supermarket, 1.25, 50, '003-discount').create_discount()
        self.assertEqual(len(myrket_supermarket.products[0].price), 1.00)
        self.assertEqual(len(myrket_supermarket.products[0].stock_quantity), 50)
        self.assertEqual(len(myrket_supermarket.products[0].sku), '003')

    def test_create_discount_must_create_a_new_discount_product_with_given_parameters(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductDiscountHandler(myrket_supermarket, 1.25, 50, '003-discount').create_discount()
        self.assertEqual(len(myrket_supermarket.products), 2)
        self.assertEqual(len(myrket_supermarket.products[1].price), 1.25)
        self.assertEqual(len(myrket_supermarket.products[1].stock_quantity), 50)
        self.assertEqual(len(myrket_supermarket.products[1].sku), '003-discount')