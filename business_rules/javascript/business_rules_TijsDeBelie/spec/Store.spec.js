const { Client, Employee } = require("../classes/Person.js")
const { Product, products, states } = require("../classes/Store.js")


var customer1;
var customer2;
var employee1;


beforeEach(function () {
    customer1 = new Client("Tijs", false)
    customer2 = new Client("Arne", true)
    employee1 = new Employee("Kris")
});


it("customer1 should have the name of Tijs", function () {
    expect(customer1.name).toEqual("Tijs");
});

it("customer1 should have 1 book in their basket for the price of 10", function () {
    customer1.addToBasket(new Product(products.BOOK, 10))
    expect(customer1.basket.length).toEqual(1);
    expect(customer1.basket[0].price).toEqual(10);
});

it("customer1 should have 3 books in their basket for the total price of 30", function () {
    customer1.addToBasket([new Product(products.BOOK, 10), new Product(products.BOOK, 10), new Product(products.BOOK, 10)])
    expect(customer1.basket.length).toEqual(3);
    expect(customer1.checkOut()).toEqual(30);
});

it("customer2 should have a member discount of 5%", function () {
    customer2.addToBasket([new Product(products.BOOK, 10, undefined, 5), new Product(products.BOOK, 10, undefined, 5), new Product(products.BOOK, 10, undefined, 5)])
    expect(customer2.basket.length).toEqual(3);
    expect(customer2.checkOut()).toEqual(30 - (30 * 0.05));
});

it("employee1 should get a commision of 5% on stuff they sell to customer1", function () {
    
    employee1.sellTo(customer1, new Product(products.BOOK, 10))
    expect(employee1.commission).toEqual(10 * 0.05);
});


