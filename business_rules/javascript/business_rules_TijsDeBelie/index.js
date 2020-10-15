const {Client, Employee} = require("./src/classes/Person.js") 
const {Product, products, states} = require("./src/classes/Store.js")

const Person1 = new Client("Tijs", false)
const Employee1 = new Employee("Kris")

Person1.addToBasket([new Product(products.BOOK, 100, undefined, 50), new Product(products.VIDEOGAME, 100, states.ONLINE, 12)]);
Person1.addToBasket(new Product(products.BOOK, 10));

Person1.checkOut();

Employee1.sellTo(Person1, [new Product(products.BOOK, 100, undefined, 50), new Product(products.VIDEOGAME, 100, states.ONLINE, 12)])





