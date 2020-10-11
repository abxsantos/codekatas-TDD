import unittest


class Product(object):
    def __init__(self):
        """
        The product will contain it's name,
        price, cost, sku, and price history.
        """
        pass


param_name_sku_list = [(1), ([]), (''), ({})]
param_cost_price_list = [("abc"), ([]), (''), ({})]


class TestSupermarket(unittest.TestCase):

    def test_product_must_raise_error_when_instantiated_with_no_properties(self):
        with self.assertRaises(TypeError):
            Product()

    def test_product_must_raise_error_when_instantiated_with_no_name(self):
        with self.assertRaises(TypeError):
            Product(name=None, cost=0.50, price=1.00, sku='001')

    def test_product_must_raise_error_when_instantiated_with_no_price(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=0.50, price=None, sku='001')

    def test_product_must_raise_error_when_instantiated_with_no_cost(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=None, price=1.00, sku='001')

    def test_product_must_raise_error_when_instantiated_with_no_sku(self):
        with self.assertRaises(TypeError):
            Product(name='beans', cost=0.50, price=1.00, sku=None)

    def test_product_must_raise_error_when_instantiated_with_sku_that_is_not_a_string(self):
        for param_sku in param_name_sku_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=0.50, price=1.00, sku=param_sku)

    def test_product_must_raise_error_when_instantiated_with_name_that_is_not_a_string(self):
        for param_name in param_name_sku_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name=param_name, cost=0.50, price=1.00, sku='123')

    def test_product_must_raise_error_when_instantiated_with_cost_that_is_not_a_number(self):
        for param_cost in param_cost_price_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=param_cost, price=1.00, sku='123')

    def test_product_must_raise_error_when_instantiated_with_price_that_is_not_a_number(self):
        for param_price in param_cost_price_list:
            with self.subTest():
                with self.assertRaises(TypeError):
                    Product(name='beans', cost=0.50, price=param_price, sku='123')

    def test_product_must_sbe_instantiated_given_correct_properties(self):
        product = Product(name='beans', cost=0.50, price=1.00, sku='001')
        self.assertEqual(product.name, 'beans')
        self.assertEqual(product.cost, 0.50)
        self.assertEqual(product.price, 1.00)
        self.assertEqual(product.sku, '001')

    def test_product_must_start_with_an_empty_price_history(self):
        product = Product(name='beans', cost=0.50, price=1.00, sku='001')
        self.assertEqual(product.price_history, [])

    def test_product_string_method_must_return_the_name(self):
        supermarket = Product(name='beans', cost=0.50, price=1.00, sku='001')
        self.assertEqual(str(supermarket), 'mYrket')


if __name__ == '__main__':
    unittest.main()

