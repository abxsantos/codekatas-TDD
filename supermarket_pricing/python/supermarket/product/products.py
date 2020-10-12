from datetime import datetime

from product.product_bundle_discount import ProductBundleDiscount


class Product(object):
    def __init__(self, name, sku, price, cost, stock_quantity, unit, bundle_discount=None):
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
        self.name: str = name
        self.sku: str = sku
        self.price: float = float(price)
        self.cost: float = float(cost)
        self.price_history: [(float, datetime)] = self._create_price_history()
        self.stock_quantity: int = stock_quantity
        self.unit: str = unit
        self.bundle_discount: ProductBundleDiscount = bundle_discount

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
