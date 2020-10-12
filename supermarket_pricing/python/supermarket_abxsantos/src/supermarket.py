class Supermarket(object):
    def __init__(self, name: str):
        """
        The supermarket_abxsantos will contain it's name and
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

