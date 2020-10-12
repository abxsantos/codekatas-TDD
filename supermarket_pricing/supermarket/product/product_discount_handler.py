import unittest

from supermarket_pricing.supermarket.product.product_inserter import ProductInserter
from supermarket_pricing.supermarket.product.products import Product
from supermarket_pricing.supermarket import Supermarket


class ProductBundleDiscountHandler(object):
    def __init__(self, product: Product, supermarket: Supermarket, discount_price=None,
                 discount_product_quantity=None, discount_product_sku=None):
        """
        Concerned with creating discounts for bundled products.
        With the newly created product with it's own sku, a validator can
        be used in the payment to handle which product price will be used.

        If the discount doesn't apply to a bundle, a modification of price
        with the ProductHistoryHandler should be used instead.

        >>> sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', unit='un',
        ... stock_quantity=100)
        >>> myrket_supermarket = Supermarket('mYrket')
        >>> ProductInserter(supermarket=myrket_supermarket, products=[sweet_potato_product]).add_products()
        >>> ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket, discount_price=1.25,
        ... discount_product_quantity=50, discount_product_sku='003-discount').create_bundle_discount()
        >>> ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket,
        ... discount_product_sku='003-discount').restore_bundle_discount_products()
        """
        self.product = product
        self.supermarket = supermarket
        self.discount_price: float = discount_price
        self.discount_product_quantity: int = discount_product_quantity
        if not discount_product_sku:
            self.discount_product_sku: str = f'{product.sku}-discount'
        else:
            self.discount_product_sku: str = discount_product_sku

    def _discount_product_creator(self) -> Product:
        """
        Create a new product entry with the given price, quantity and sku
        the new product should have the same unit and cost
        :return discount_product: created product that can be used for bundle discounts
        """
        discount_product = Product(name=self.product.name,
                                   stock_quantity=self.discount_product_quantity,
                                   price=self.discount_price,
                                   unit=self.product.unit,
                                   cost=self.product.cost,
                                   sku=self.discount_product_sku)
        ProductInserter(supermarket=self.supermarket, products=[discount_product]).add_products()
        return discount_product

    def create_bundle_discount(self) -> Product:
        """
        Must create a discount product entry into
        the supermarket with discount price and quantity
        that will be removed from the stock quantity of original product
        """
        if self.discount_product_quantity > self.product.stock_quantity:
            raise ValueError('The discount product quantity is smaller than what is available in stock')
        self.product.stock_quantity -= self.discount_product_quantity
        return self._discount_product_creator()

    def restore_bundle_discount_products(self) -> Product:
        """
        Restores the given discount product
        to it's original product stock quantity
        """
        for discount_product in self.supermarket.products:
            if discount_product.sku == self.discount_product_sku:
                self.product.stock_quantity += discount_product.stock_quantity
                discount_product.stock_quantity = 0
                return self.product


class TestProductDiscountHandler(unittest.TestCase):
    def test_create_discount_must_change_the_quantity_of_product(self):
        sweet_potato_product = Product(name='sweet potato', cost=0.50, price=1.00, sku='003', unit='un',
                                       stock_quantity=100)
        myrket_supermarket = Supermarket('mYrket')
        ProductInserter(supermarket=myrket_supermarket,
                        products=[sweet_potato_product]).add_products()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket, discount_price=1.25,
                                     discount_product_quantity=50, discount_product_sku='003-discount').create_bundle_discount()
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
                                     discount_product_quantity=50, discount_product_sku='003-discount').create_bundle_discount()
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
                                     discount_product_quantity=50, discount_product_sku='003-discount').create_bundle_discount()
        ProductBundleDiscountHandler(product=sweet_potato_product, supermarket=myrket_supermarket,
                                     discount_product_sku='003-discount').restore_bundle_discount_products()
        self.assertEqual(len(myrket_supermarket.products), 2)
        self.assertEqual(myrket_supermarket.products[0].price, 1.00)
        self.assertEqual(myrket_supermarket.products[0].stock_quantity, 100)
        self.assertEqual(myrket_supermarket.products[0].sku, '003')
        self.assertEqual(myrket_supermarket.products[1].price, 1.25)
        self.assertEqual(myrket_supermarket.products[1].stock_quantity, 0)
        self.assertEqual(myrket_supermarket.products[1].sku, '003-discount')
