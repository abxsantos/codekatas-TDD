import unittest


class Supermarket(object):
    """
    The supermarket will contain it's name and
    all the products registered in it.
    """
    pass


class TestSupermarket(unittest.TestCase):

    def test_supermaket_is_instantiated_with_given_name(self):
        supermarket = Supermarket('mYrket')
        self.assertEqual(supermarket.name, 'mYrket')


if __name__ == '__main__':
    unittest.main()

