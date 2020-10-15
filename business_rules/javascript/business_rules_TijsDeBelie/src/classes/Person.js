const {states} = require("./Store.js")


class Person {
  constructor(name) {
    this.name = name;
  }
}

class Client extends Person {
 constructor(name, membership = false) {
    super(name);
    this.membership = membership;
    this.basket = [];
  }

    addToBasket = (product) => {

        if(Object.prototype.toString.call(product) == "[object Array]"){
            product.forEach(product => {
                 this.basket.push(product);
            });
        }else{
            this.basket.push(product);
            console.log(this.basket)
        }
        
    }

    checkOut = () =>{
        let total = 0;
        this.basket.forEach(product => {
            total += (this.membership ? product.discount !== 0 ? product.price - (product.price * product.discount /100) : product.price : product.price);
        })

        return total;
    }
}

class Employee extends Person {
    constructor(name, commission = 0) {
    super(name);

    this.commission = commission;
  }


sellTo = (person, product) => {

   
    if(Object.prototype.toString.call(product) == "[object Array]"){
       
        product.forEach(product => {
             if(product.state == states.PHYSICAL){
                 console.log("PRICE", product.price)
                this.commission += product.price * 0.05;
             }
             person.addToBasket(product);
        });
    }else{
        person.addToBasket(product);
    }

    if(product.state == states.PHYSICAL){
        console.log("PRICE", product.price)
        this.commission += product.price * 0.05;
    }
    return this.commission;

};

}

module.exports = {
Client : Client,
Employee : Employee
}