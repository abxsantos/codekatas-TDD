from src.product.products import Product


class CartProduct(object):
    def __init__(self, product: Product, quantity: int):
        """Client cart item"""
        self.product = product
        self.quantity = quantity
        self._remove_item_from_stock(quantity_to_remove=self.quantity)

    def _remove_item_from_stock(self, quantity_to_remove: int):
        if quantity_to_remove > self.product.stock_quantity:
            raise ValueError('There are no more products left in the stock')
        self.product.stock_quantity -= quantity_to_remove

    def restore_item_to_stock(self, removed_quantity: int):
        if self.quantity > 0:
            self.product.stock_quantity += removed_quantity
            self.quantity -= removed_quantity

    def increase_quantity(self, added_quantity: int):
        """Increases the quantity of a cart product"""
        self._remove_item_from_stock(quantity_to_remove=added_quantity)
        self.quantity += added_quantity

    def __str__(self):
        return self.product.name


