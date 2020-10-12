import unittest


class ProductBundleDiscount(object):
    def __init__(self, bundle_quantity, bundle_price):
        self.bundle_quantity: int = self._validate(parameter=bundle_quantity)
        self.bundle_price: float = self._validate(parameter=bundle_price)

    @staticmethod
    def _validate(parameter):
        if parameter < 0:
            raise ValueError('Price must be a positive number')
        return parameter
