import unittest


class Supermarket(object):
    def __init__(self, name):
        """
        The supermarket will contain it's name and
        all the products registered in it.
        """
        self.name = name


class TestSupermarket(unittest.TestCase):

    def test_supermaket_is_instantiated_with_given_name(self):
        supermarket = Supermarket('mYrket')
        self.assertEqual(supermarket.name, 'mYrket')

    def test_supermaket_must_raise_error_when_no_name_is_given(self):
        with self.assertRaises(TypeError):
            Supermarket()


if __name__ == '__main__':
    unittest.main()

