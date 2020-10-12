import unittest


class Supermarket(object):
    def __init__(self, name: str):
        """
        The supermarket will contain it's name and
        all the products registered in it.

        >>> my_markek = Supermarket('mYrket')
        >>> my_markek.name = 'mYrket'
        >>> my_markek.products = []
        """
        self.name = name
        self.products = []

    def __str__(self) -> str:
        """Returns the name of the supermarket"""
        return self.name


class TestSupermarket(unittest.TestCase):

    def test_supermaket_is_instantiated_with_given_name(self):
        supermarket = Supermarket('mYrket')
        self.assertEqual(supermarket.name, 'mYrket')

    def test_supermaket_must_raise_error_when_no_name_is_given(self):
        with self.assertRaises(TypeError):
            Supermarket()

    def test_supermaket_must_be_instantiated_with_no_products(self):
        supermarket = Supermarket('mYrket')
        self.assertEqual(supermarket.products, [])

    def test_supermarket_string_method_must_return_the_name(self):
        supermarket = Supermarket('mYrket')
        self.assertEqual(str(supermarket), 'mYrket')


if __name__ == '__main__':
    unittest.main()

