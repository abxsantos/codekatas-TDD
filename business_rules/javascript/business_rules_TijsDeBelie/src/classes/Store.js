const products = {
    BOOK: 'Book',
    VIDEOGAME: 'Videogame',
    BANANA: 'Banana'
}

const states = {
    ONLINE: 'Online',
    PHYSICAL: 'Physical'
}


class Product {
  constructor(name, price = 0, state = states.PHYSICAL, discount = 0) {
    this.name = name;
    this.state = state;
    this.price = price;
    this.discount = discount;
  }

}


module.exports = {
    Product : Product,
    products : products,
    states : states
}