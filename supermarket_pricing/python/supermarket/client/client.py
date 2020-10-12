from cart.cart import CartProduct
from product.products import Product


class Client(object):
    def __init__(self, name, wallet=None):
        """
        Supermarket client
        >>> wilson = Client(name='Wilson', wallet=10.00)
        >>> sweet_potato = Product(name='sweet_potato', sku='001', price=1.00, cost=0.50, stock_quantity=100, unit='Kg')
        >>> cart_sweet_potato = CartProduct(product=sweet_potato, quantity=1)
        >>> wilson.add_product_to_cart(cart_sweet_potato, 1)
        >>> wilson.pay()
        """
        self.name: str = name
        self.cart: set = set()
        self.wallet: float = wallet

    @staticmethod
    def _create_cart_product(added_product: Product, added_quantity: int) -> CartProduct:
        """
        Creates a cart product with given product and quantity
        :param added_product: Product that will be used to create the cart product
        :param added_quantity: Quantity of the product
        :return: Cart product
        """
        return CartProduct(product=added_product, quantity=added_quantity)

    def _search_product(self, product: Product) -> CartProduct:
        """Searches the cart for the given product"""
        for cart_product in self.cart:
            if cart_product.product == product:
                return cart_product

    def add_product_to_cart(self, added_product: Product, added_quantity: int):
        """Adds a given product to client cart"""
        cart_product = self._search_product(added_product)
        if cart_product:
            cart_product.increase_quantity(added_quantity=added_quantity)
        else:
            cart_product = self._create_cart_product(added_product, added_quantity)
            self.cart.add(cart_product)

    def remove_product_from_cart(self, product: Product, removed_quantity: int):
        cart_product = self._search_product(product)
        if removed_quantity == cart_product.quantity:
            self.cart.remove(cart_product)
        cart_product.restore_item_to_stock(removed_quantity)

    def _calculate_cart_price(self) -> float:
        """Calculates the cart total value"""
        total_price = 0
        for cart_product in self.cart:
            total_price += (cart_product.product.price * cart_product.quantity)
        return total_price

    # TODO: Refactor this to handle logic of bundle discount products
    def pay(self):
        """
        Pays for the cart total value
        :raises Exception: When the client has no money
        """
        total_price = self._calculate_cart_price()
        if total_price > self.wallet:
            raise Exception('Not enough money in the wallet!')
        self.wallet -= total_price
