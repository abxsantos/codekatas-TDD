import unittest
from datetime import datetime


class Product(object):
    def __init__(self, name: str, sku: str, price: float, cost: float, stock_quantity: int, unit: str):
        """
        The product will contain it's name,
        price, cost, sku, and price history.
        >>> sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        >>> sweet_potato.name = 'sweet_potato'
        >>> sweet_potato.price = 1.00
        >>> sweet_potato.cost = 0.50
        >>> sweet_potato.sku = '001'
        >>> sweet_potato.stock_quantity = 100
        >>> sweet_potato.unit = 'Kg'
        """
        self._validate_values(name, sku, price, cost)
        self.name = name
        self.sku = sku
        self.price = float(price)
        self.cost = float(cost)
        self.price_history = self._create_price_history()
        self.stock_quantity = stock_quantity
        self.unit = unit

    @staticmethod
    def _validate_values(name: str, sku: str, price: float, cost: float):
        """
        Validates the class initializer parameters
        :param name: name of the product
        :param sku: stock keeping unit code
        :param price: price that the consumer will pay for the product
        :param cost: cost that the owner paid for the product
        :raises TypeError:
        """
        if not name or not isinstance(name, str):
            raise TypeError('A correct name must be provided')
        if not sku or not isinstance(sku, str):
            raise TypeError('SKU must be provided')
        if not price or not isinstance(price, (float, int)):
            raise TypeError('Price must be provided')
        if not cost or not isinstance(cost, (float, int)):
            raise TypeError('Cost must be provided')

    def _create_price_history(self):
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return [(self.price, now)]

    def __str__(self) -> str:
        return self.name


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


if __name__ == '__main__':
    unittest.main()

