import unittest

from product.product_inserter import ProductInserter
from product.products import Product
from supermarket import Supermarket


class TestProductInserter(unittest.TestCase):
    def test_batch_add_product_must_insert_a_product_into_supermaket_products_list(self):
        bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001', stock_quantity=100, unit='Kg')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket, products=[bean_product]).add_products()
        self.assertEqual(len(myrket_supermarket.products), 1)

    def test_batch_add_product_must_insert_a_list_of_products_into_supermaket_products_list(self):
        bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001', stock_quantity=100, unit='Kg')
        rice_product = Product(name='rice', cost=0.50, price=1.00, sku='002', stock_quantity=100, unit='Kg')
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', stock_quantity=100,
                                       unit='Kg')
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[bean_product, rice_product, sweet_potato_product]).add_products()
        self.assertEqual(len(myrket_supermarket.products), 3)

    def test_add_product_must_raise_typeerror_if_no_products_are_given(self):
        myrket_supermarket = Supermarket('mYrket')
        with self.assertRaises(TypeError):
            ProductInserter(supermarket=myrket_supermarket, products=None).add_products()


if __name__ == '__main__':
    unittest.main()