import unittest

from product.product_bundle_discount import ProductBundleDiscount


class TestBundleDiscount(unittest.TestCase):
    def test_bundle_discount(self):
        bundle_discount = ProductBundleDiscount(bundle_quantity=2, bundle_price=0.50)
        self.assertEqual(bundle_discount.bundle_quantity, 2)
        self.assertEqual(bundle_discount.bundle_price, 0.50)

    def test_bundle_discount_must_raise_exception_given_negative_price(self):
        with self.assertRaises(ValueError):
            ProductBundleDiscount(bundle_quantity=2, bundle_price=-0.50)

    def test_bundle_discount_must_raise_exception_given_negative_quantity(self):
        with self.assertRaises(ValueError):
            ProductBundleDiscount(bundle_quantity=-2, bundle_price=0.50)
