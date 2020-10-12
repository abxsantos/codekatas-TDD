import unittest

from product.product_discount_handler import ProductBundleDiscountHandler
from product.product_inserter import ProductInserter
from product.products import Product
from supermarket import Supermarket


class TestProductDiscountHandler(unittest.TestCase):
    def test_create_discount_must_change_the_quantity_of_product(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', unit='un',
                                       stock_quantity=100)
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket, discount_price=1.25,
                                     discount_product_quantity=50,
                                     discount_product_sku='003-discount').create_bundle_discount()
        self.assertEqual(myrket_supermarket.products[0].price, 1.00)
        self.assertEqual(myrket_supermarket.products[0].stock_quantity, 50)
        self.assertEqual(myrket_supermarket.products[0].sku, '003')

    def test_create_discount_must_create_a_new_discount_product_with_given_parameters(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', unit='un',
                                       stock_quantity=100)
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket, discount_price=1.25,
                                     discount_product_quantity=50,
                                     discount_product_sku='003-discount').create_bundle_discount()
        self.assertEqual(len(myrket_supermarket.products), 2)
        self.assertEqual(myrket_supermarket.products[1].price, 1.25)
        self.assertEqual(myrket_supermarket.products[1].stock_quantity, 50)
        self.assertEqual(myrket_supermarket.products[1].sku, '003-discount')

    def test_restore_discount_product_must_restore_the_stock_quantity_of_original_with_given_parameters(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', unit='un',
                                       stock_quantity=100)
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket, discount_price=1.25,
                                     discount_product_quantity=50,
                                     discount_product_sku='003-discount').create_bundle_discount()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket,
                                     discount_product_sku='003-discount').restore_bundle_discount_products()
        self.assertEqual(len(myrket_supermarket.products), 2)
        self.assertEqual(myrket_supermarket.products[0].price, 1.00)
        self.assertEqual(myrket_supermarket.products[0].stock_quantity, 100)
        self.assertEqual(myrket_supermarket.products[0].sku, '003')
        self.assertEqual(myrket_supermarket.products[1].price, 1.25)
        self.assertEqual(myrket_supermarket.products[1].stock_quantity, 0)
        self.assertEqual(myrket_supermarket.products[1].sku, '003-discount')
