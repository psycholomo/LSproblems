/*
### 1. Basic: What are the main advantages of using factory functions for object creation in JavaScript?

the main advantage is the simplicity, the object is always created, you can call it as many times as you want and dont have to worry about inheritance.
allows for excapsulation to create closures and private variables
no confusion with this


### 2. Basic: What are two disadvantages of working with factory functions?

memory ineffecient as all methods belong to the object, if you want to use inheritance it is clunky, no types with object creation. cant use instance of


### 3. Intermediate: Explain why objects created by factory functions are said to not have a specific "type". How does this affect the use of instanceof and the constructor property on these objects?
The problem when created with factory functions is they are created with Object.create so they are just plain objects that dont have a constructor. The prototype points to the top object

function makeDog(name) {
return name
while objects created from an object factory cant have an instance of it. its just a new object.

constructorDog.constructor === Dog
factoryDog.constructor === makeDog == false
factoryDog.constructor === Object is true as its just a plain object
}



### 4. Intermediate: A colleague argues that factory functions are not ideal because every object created gets its own copy of all methods, potentially using more memory. Explain this disadvantage with a code example and describe a scenario where this might not be a significant concern.

*/

// import {subtract, add } from "./test.js" 

// console.log(add(1,2))

// function delegate(obj, meth, ...args) {
//     return function(...moreArgs) {
//         let result = args.concat(moreArgs)
//         return object[meth].apply(obj,result)
//     }
// }


// let boo = {}
// boo.myProp = 1;
// let far = Object.create(boo)
// far.hasOwnProperty('myProp')
// Object.getOwnPropertyNames(far).includes('myProp')

// function createObject(obj) {
//     function F() {

//     }
//     F.prototype = obj
//     return new F()
// }

// function neww(constructor, args) {
//   let object = Object.create(constructor.prototype);
//   let result = constructor.apply(object, args);
  
//   return (typeof result === 'object' && result !== null) ? result : object;
// }

// function Circle(radius) {
//     this.radius = radius
// }

// Circle.prototype.area = function() {
//     return 3.14 * this.radius * this.radius
//}

// in this example we are setting the prototype of area on the constructor function of circle.
// When we call new we are effectively creating a new instance object by calling the constructor function and setting the prototype of that object to the Circle object.\


// function getDefiningObject(object, propKey) {

//     let obj = Object.hasOwnProperty(propKey)
    

//     while (object) {
//             if (object.hasOwnProperty(propKey)) {

//             return object
//             }
//     object = Object.getPrototypeOf(object)
//     obj = Object.hasOwnProperty(propKey)
//     }

//     return null

//   // ...
// }

// let foo = {
//   a: 1,
//   b: 2,
// };

// let bar = Object.create(foo);
// let baz = Object.create(bar);
// let qux = Object.create(baz);

// bar.c = 3;

// console.log(getDefiningObject(qux, 'c') === bar);     // => true
// console.log(getDefiningObject(qux, 'e'));             // => null

// function shallowCopy(object) {
//     let obj = {}
//     let properties = Object.getOwnPropertyNames(object)
//     for (let i = 0; i < properties.length; i += 1) {
//         obj[properties[i]] = object[properties[i]]
//     }

//     return obj
// }


// let foo = {
//   a: 1,
//   b: 2,
// };

// let bar = Object.create(foo);
// bar.c = 3;
// bar.say = function() {
//   console.log('c is ' + this.c);
// };

// let baz = shallowCopy(bar);
// console.log(baz)
// console.log(baz.a);       // => 1
// baz.say();                // => c is 3
// baz.hasOwnProperty('a');  // false
// baz.hasOwnProperty('b');  // false
// baz.hasOwnProperty('c');  // true

// function shallowCopy(object) {
//     let copy = Object.create(Object.getPrototypeOf(object))

//     Object.getOwnPropertyNames(object).forEach(prop => {
//         copy[prop] = object[prop]
//     })
// }

// Object.prototype.begetObject = function() {
//     function F() {}
//     F.prototype = this;
//     return new F();
// }

// let foo = {
//     a: 1,
// }

// let bar = foo.begetObject();
// foo.isProtototypeOf(bar)
// it uses a constroctur function to create a new object with this as its prototype. this is the same as using "Object.create"


// function Person(name) {
//   this.name = name;
//   this.friends = [];
// }

// let alice = new Person("Alice");
// let bob = new Person("Bob");

// Person.prototype.friends.push("Charlie");

// console.log(alice.friends); // ?
// console.log(bob.friends);   // ?

// let animal = {
//   eats: true
// };

// let rabbit = Object.create(animal);

// console.log(Object.getPrototypeOf(rabbit))
// delete rabbit.eats;

// console.log(rabbit.eats);




//  function PetPrototype(animal, name) {
//     this.animal = animal
//     this.name = name

//  }


//   PetPrototype.prototype.sleep = function() {
//     console.log("I am sleeping");
//   }

//   PetPrototype.prototype.wake = function() {
//     console.log("I am awake");
//   }

//   let dog = new PetPrototype('dog', 'rover')



// function Person(firstName, lastName, age, gender) {
//     this.firstName = firstName


// }

// function Doctor(firstName, lastName) {
//     Person.call(this, firstName, lastName)
// }


// Doctor.prototype = Object.create(Person.prototype)
// Doctor.prototype.constructor = Doctor


// Object.getOwnPropertyNames(obj)
// Object.getPrototypeOf(Doctor)
// Object.setPrototypeOf(value, foo)

// Object.assign when you want to use methods from multiple sources


// function User(first, last) {
//   if (!(this instanceof User)) {
//     return new User(first, last);
//   }
  
//   this.name = first + ' ' + last;
// }



// **Question:** Explain the purpose of the constructor method within a JavaScript class. When is it automatically called?

// **Answer:**
// The `constructor` method is a special method used for initializing new instances of a class. Its purposes are:

// 1. **Initialize instance properties** - Set up the initial state of the object
// 2. **Accept parameters** - Receive arguments passed when creating a new instance
// 3. **Set up initial configurations** - Perform any setup logic needed

// The constructor is **automatically called when a new instance is created** using the `new` keyword.

// constructor functions are functions invoked with new. it assigns properties and returns an object.

// when you create a new object it calls the constructor function. that contains a constructor and the methods are assigned to the function prototype prototype.

// functions have a prototype property
// All objects have an object property, object prototype for an object is an object that contains the methods for the methods an it inherits.

// function prototypes also have object prototypes. By default, the object prototype of a function prototype is the function prototype of the superclass.

// In JavaScript, every object has a hidden property called [[Prototype]] that points to its object prototype or null.


// function prototypes are used when creating new objects from the function or class; the function prototype gets assigned as the object prototype for the newly created object. 
// Object prototypes are used by objects to define where JavaScript should look for instance methods. Function.prototype


