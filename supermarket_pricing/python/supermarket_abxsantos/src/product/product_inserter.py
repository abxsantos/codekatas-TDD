from src.product.products import Product
from src.supermarket import Supermarket


class ProductInserter(object):
    def __init__(self, supermarket: Supermarket, products: [Product]):
        """
        Used to insert products into the supermarket_abxsantos.
        Concerned with adding a new product to the supermarket_abxsantos.

        >>> bean_product = Product(name='beans', cost=0.50, price=1.00, sku='001', unit='un', stock_quantity=100)
        >>> myrket_supermarket = Supermarket('mYrket')
        >>> ProductInserter(supermarket_abxsantos=myrket_supermarket, products=[bean_product]).add_products()
        >>> myrket_supermarket.products[0].name = 'beans'
        """
        self.products = products
        self.supermarket = supermarket

    def add_products(self):
        for product in self.products:
            self.supermarket.products.append(product)


