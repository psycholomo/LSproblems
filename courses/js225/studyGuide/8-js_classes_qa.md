# JavaScript Classes - Questions & Answers

## Basic Questions

### 1. Basic Cat Class
**Question:** Create a class Cat that logs the string `I'm a cat!` to the console whenever a new instance is created. Then instantiate a new instance of Cat and assign it to a kitty variable.

**Answer:**
```javascript
class Cat {
  constructor() {
    console.log("I'm a cat!");
  }
}

let kitty = new Cat(); // I'm a cat!
```

### 2. Cat with Name Parameter
**Question:** Using the code from the previous exercise, add a parameter to constructor that provides a name for the Cat object, and assign this parameter to a property called name. If no argument is provided, the name should default to Kitty. Then, replace the `I'm a cat!` message with a greeting that includes the provided name.

**Answer:**
```javascript
class Cat {
  constructor(name = 'Kitty') {
    this.name = name;
    console.log(`Hello! My name is ${this.name}!`);
  }
}

let kitty = new Cat(); // Hello! My name is Kitty!
let fluffy = new Cat('Fluffy'); // Hello! My name is Fluffy!
```

### 3. Instance Methods - greet and rename
**Question:** Move the greeting from the constructor method to an instance method named `greet` that logs a greeting to the console when invoked. Additionally, define one more instance method named `rename` that renames a Cat instance when invoked.

**Answer:**
```javascript
class Cat {
  constructor(name = 'Kitty') {
    this.name = name;
  }

  greet() {
    console.log(`Hello! My name is ${this.name}!`);
  }

  rename(newName) {
    this.name = newName;
  }
}

// Expected behavior
let kitty = new Cat();
kitty.greet(); // Hello! My name is Kitty!
kitty.rename('Sophie');
kitty.greet(); // Hello! My name is Sophie!
```

### 4. Static Method
**Question:** Using the code from the previous question, write any code necessary so that the string `Hello! I'm a cat!` is logged to the console when `Cat.genericGreeting` is invoked.

**Answer:**
```javascript
class Cat {
  constructor(name = 'Kitty') {
    this.name = name;
  }

  greet() {
    console.log(`Hello! My name is ${this.name}!`);
  }

  rename(newName) {
    this.name = newName;
  }

  static genericGreeting() {
    console.log("Hello! I'm a cat!");
  }
}

Cat.genericGreeting(); // Hello! I'm a cat!
```

### 5. Rectangle Class
**Question:** Create a class Rectangle. The constructor should take 2 arguments which represent width and length, respectively. Implement the class so that the output from the example below is correct.

**Answer:**
```javascript
class Rectangle {
  constructor(width, length) {
    this.width = width;
    this.length = length;
  }

  getWidth() {
    return this.width;
  }

  getLength() {
    return this.length;
  }

  getArea() {
    return this.width * this.length;
  }
}

let rect = new Rectangle(4, 5);
console.log(rect.getWidth()); // 4
console.log(rect.getLength()); // 5
console.log(rect.getArea()); // 20
```

## Intermediate Questions

### 6. Pet and Cat Inheritance
**Question:** Update the code so that when you run it, you see the specified output.

**Answer:**
```javascript
class Pet {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}

class Cat extends Pet {
  constructor(name, age, colors) {
    super(name, age);
    this.colors = colors;
  }

  info() {
    return `My cat ${this.name} is ${this.age} years old and has ${this.colors} fur.`;
  }
}

let pudding = new Cat('Pudding', 7, 'black and white');
let butterscotch = new Cat('Butterscotch', 10, 'tan and white');

console.log(pudding.info());
// My cat Pudding is 7 years old and has black and white fur.
console.log(butterscotch.info());
// My cat Butterscotch is 10 years old and has tan and white fur.
```

### 7. Animal, Cat, and Dog Classes
**Question:** Given a class Animal, create two classes Cat and Dog that inherit from it. The Cat constructor should take 3 arguments (name, age, status). The Dog constructor should take 4 arguments (name, age, status, master).

**Answer:**
```javascript
class Animal {
  constructor(name, age, legs, species, status) {
    this.name = name;
    this.age = age;
    this.legs = legs;
    this.species = species;
    this.status = status;
  }
  introduce() {
    return `Hello, my name is ${this.name} and I am ${this.age} years old and ${this.status}.`;
  }
}

class Cat extends Animal {
  constructor(name, age, status) {
    super(name, age, 4, 'cat', status);
  }

  introduce() {
    return super.introduce() + ' Meow meow!';
  }
}

class Dog extends Animal {
  constructor(name, age, status, master) {
    super(name, age, 4, 'dog', status);
    this.master = master;
  }

  greetMaster() {
    return `Hello ${this.master}! Woof, woof!`;
  }
}

// Testing
let cat = new Cat('Whiskers', 3, 'happy');
console.log(cat.introduce());
// Hello, my name is Whiskers and I am 3 years old and happy. Meow meow!

let dog = new Dog('Buddy', 5, 'excited', 'John');
console.log(dog.introduce());
// Hello, my name is Buddy and I am 5 years old and excited.
console.log(dog.greetMaster());
// Hello John! Woof, woof!
```

## Advanced Questions

### 8. Banner Class
**Question:** Complete the Banner class so that the test cases work as intended.

**Answer:**
```javascript
class Banner {
  constructor(message) {
    this.message = message;
  }

  displayBanner() {
    console.log([
      this.horizontalRule(),
      this.emptyLine(),
      this.messageLine(),
      this.emptyLine(),
      this.horizontalRule()
    ].join("\n"));
  }

  horizontalRule() {
    return `+${'-'.repeat(this.message.length + 2)}+`;
  }

  emptyLine() {
    return `|${' '.repeat(this.message.length + 2)}|`;
  }

  messageLine() {
    return `| ${this.message} |`;
  }
}

// Test Cases
let banner1 = new Banner('To boldly go where no one has gone before.');
banner1.displayBanner();
// +--------------------------------------------+
// |                                            |
// | To boldly go where no one has gone before. |
// |                                            |
// +--------------------------------------------+

let banner2 = new Banner('');
banner2.displayBanner();
// +--+
// |  |
// |  |
// |  |
// +--+
```

### 9. Object Without new
**Question:** Without calling `new Cat()`, create an object that uses `Cat.prototype` for its prototype. Log the object and the result of calling `speaks()` on it. What is missing from this "fake" instance?

**Answer:**
```javascript
class Cat {
  constructor(name) {
    this.name = name;
  }
  speaks() {
    return `${this.name} says meowwww.`;
  }
}

// Create object without new
let fakeCat = Object.create(Cat.prototype);
console.log(fakeCat); // Cat {} - empty object
console.log(fakeCat.speaks()); // undefined says meowwww.

// What's missing?
// The constructor was never called, so the 'name' property was never initialized.
// The object has access to the prototype methods but lacks instance properties.

// To fix it, we could manually set the property:
fakeCat.name = 'Whiskers';
console.log(fakeCat.speaks()); // Whiskers says meowwww.
```

## Conceptual Questions

### 10. Class Keyword
**Question:** What is the class keyword in JavaScript, and what object creation pattern is it considered "syntactic sugar" for?

**Answer:**
The `class` keyword in JavaScript is syntactic sugar for the **constructor function pattern** combined with **prototypal inheritance**. 

Behind the scenes, classes are still based on JavaScript's prototype system. When you create a class, JavaScript creates a constructor function and sets up the prototype chain. For example:

```javascript
// Using class syntax
class Person {
  constructor(name) {
    this.name = name;
  }
  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }
}

// Is equivalent to:
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  console.log(`Hello, I'm ${this.name}`);
};
```

### 11. Constructor Method
**Question:** Explain the purpose of the constructor method within a JavaScript class. When is it automatically called?

**Answer:**
The `constructor` method is a special method used for initializing new instances of a class. Its purposes are:

1. **Initialize instance properties** - Set up the initial state of the object
2. **Accept parameters** - Receive arguments passed when creating a new instance
3. **Set up initial configurations** - Perform any setup logic needed

The constructor is **automatically called when a new instance is created** using the `new` keyword.

```javascript
class Car {
  constructor(make, model) {
    this.make = make;
    this.model = model;
    console.log('Constructor called!');
  }
}

let myCar = new Car('Toyota', 'Camry'); // Constructor called!
// The constructor runs immediately and initializes make and model
```

**Important notes:**
- There can only be one constructor per class
- If you don't define a constructor, JavaScript provides a default empty one
- In a subclass, you must call `super()` before accessing `this`

### 12. Instance vs Static Methods
**Question:** What is the difference between an instance method and a static method in a class? Provide a code example for defining and calling each type of method.

**Answer:**

**Instance Methods:**
- Called on instances of the class
- Have access to instance properties via `this`
- Each instance can have different data but shares the same method

**Static Methods:**
- Called on the class itself, not on instances
- Do NOT have access to instance properties
- Used for utility functions or factory methods related to the class

```javascript
class MathHelper {
  constructor(value) {
    this.value = value;
  }

  // Instance method - called on instances
  double() {
    return this.value * 2;
  }

  // Static method - called on the class itself
  static add(a, b) {
    return a + b;
  }

  static createWithValue(value) {
    return new MathHelper(value);
  }
}

// Instance method usage
let helper = new MathHelper(5);
console.log(helper.double()); // 10

// Static method usage
console.log(MathHelper.add(3, 7)); // 10
let newHelper = MathHelper.createWithValue(10);
console.log(newHelper.double()); // 20

// This would throw an error:
// console.log(helper.add(3, 7)); // TypeError: helper.add is not a function
// console.log(MathHelper.double()); // TypeError: MathHelper.double is not a function
```

### 13. Super Keyword
**Question:** In the context of class inheritance, what is the purpose of the `super()` keyword? Provide an example of its use in a constructor and an example of its use for calling a method from the superclass.

**Answer:**

The `super` keyword is used to:
1. **Call the parent class constructor** - `super()` in a constructor
2. **Access parent class methods** - `super.methodName()` anywhere in the subclass

**Example 1: Using super() in a constructor**
```javascript
class Vehicle {
  constructor(type, wheels) {
    this.type = type;
    this.wheels = wheels;
  }
}

class Car extends Vehicle {
  constructor(make, model) {
    super('car', 4); // Calls Vehicle constructor
    this.make = make;
    this.model = model;
  }
}

let myCar = new Car('Honda', 'Civic');
console.log(myCar.type); // 'car'
console.log(myCar.wheels); // 4
```

**Example 2: Using super to call parent methods**
```javascript
class Animal {
  speak() {
    return 'Some sound';
  }

  move() {
    return 'Moving...';
  }
}

class Dog extends Animal {
  speak() {
    return super.speak() + ' - Woof!'; // Calls parent's speak method
  }

  fetch() {
    console.log(super.move()); // Calls parent's move method
    return 'Fetching the ball';
  }
}

let dog = new Dog();
console.log(dog.speak()); // 'Some sound - Woof!'
console.log(dog.fetch()); // Logs 'Moving...', returns 'Fetching the ball'
```

**Important:** In a subclass constructor, you MUST call `super()` before accessing `this`.

### 14. Extends Keyword
**Question:** What does the `extends` keyword do in a class declaration?

**Answer:**

The `extends` keyword establishes **inheritance** between classes by:

1. **Setting up the prototype chain** - The subclass prototype inherits from the superclass prototype
2. **Enabling method inheritance** - The subclass inherits all methods from the superclass
3. **Allowing method overriding** - The subclass can override parent methods while still accessing them via `super`

```javascript
class Shape {
  constructor(color) {
    this.color = color;
  }

  describe() {
    return `A ${this.color} shape`;
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }

  getArea() {
    return Math.PI * this.radius ** 2;
  }

  describe() {
    return super.describe() + ` with radius ${this.radius}`;
  }
}

let circle = new Circle('red', 5);
console.log(circle.describe()); // 'A red shape with radius 5'
console.log(circle.getArea()); // 78.53981633974483

// Prototype chain: circle -> Circle.prototype -> Shape.prototype -> Object.prototype
console.log(circle instanceof Circle); // true
console.log(circle instanceof Shape); // true
console.log(circle instanceof Object); // true
```

### 15. Behavior Delegation
**Question:** What is behavior delegation and how does it relate to classes and prototypes in JavaScript?

**Answer:**

**Behavior delegation** is the mechanism by which objects can delegate property and method lookups to other objects through the prototype chain. It's the foundation of how JavaScript implements inheritance.

**How it works:**
1. When you access a property/method on an object, JavaScript first looks on the object itself
2. If not found, it looks at the object's prototype
3. This continues up the prototype chain until the property is found or the chain ends (at `Object.prototype`)

**Relationship to Classes:**
Classes in JavaScript use behavior delegation behind the scenes. When you create a class, methods are added to the prototype, allowing all instances to delegate to the same method implementations.

```javascript
class Animal {
  constructor(name) {
    this.name = name;
  }

  eat() {
    return `${this.name} is eating`;
  }
}

class Dog extends Animal {
  constructor(name, breed) {
    super(name);
    this.breed = breed;
  }

  bark() {
    return `${this.name} says woof!`;
  }
}

let dog = new Dog('Buddy', 'Golden Retriever');

// Property lookup chain:
console.log(dog.name); // Found on the instance itself
console.log(dog.bark()); // Delegates to Dog.prototype
console.log(dog.eat()); // Delegates to Animal.prototype (via Dog.prototype)

// Behind the scenes:
console.log(dog.hasOwnProperty('name')); // true - own property
console.log(dog.hasOwnProperty('bark')); // false - inherited from Dog.prototype
console.log(dog.hasOwnProperty('eat')); // false - inherited from Animal.prototype

// The delegation chain:
// dog -> Dog.prototype -> Animal.prototype -> Object.prototype -> null
```

**Key Points:**
- Objects don't copy methods; they delegate to their prototype
- Multiple objects can share the same prototype, saving memory
- This is more memory-efficient than copying methods to each instance
- JavaScript's inheritance is fundamentally different from classical inheritance in languages like Java or C++

---

## Additional Tricky Questions

### 16. Private Fields and Methods
**Question:** Implement a `BankAccount` class using private fields (ES2022+) with a private `#balance` property and a private `#validateAmount()` method. The class should have public methods to deposit, withdraw, and check balance.

**Answer:**
```javascript
class BankAccount {
  #balance = 0;

  constructor(initialBalance = 0) {
    this.#balance = initialBalance;
  }

  #validateAmount(amount) {
    if (typeof amount !== 'number' || amount <= 0) {
      throw new Error('Amount must be a positive number');
    }
  }

  deposit(amount) {
    this.#validateAmount(amount);
    this.#balance += amount;
    return `Deposited $${amount}. New balance: $${this.#balance}`;
  }

  withdraw(amount) {
    this.#validateAmount(amount);
    if (amount > this.#balance) {
      throw new Error('Insufficient funds');
    }
    this.#balance -= amount;
    return `Withdrew $${amount}. New balance: $${this.#balance}`;
  }

  getBalance() {
    return this.#balance;
  }
}

let account = new BankAccount(100);
console.log(account.deposit(50)); // Deposited $50. New balance: $150
console.log(account.getBalance()); // 150
// console.log(account.#balance); // SyntaxError: Private field '#balance' must be declared in an enclosing class
```

### 17. Method Chaining
**Question:** Create a `Calculator` class that supports method chaining for operations (add, subtract, multiply, divide) and has a `result()` method to get the final value.

**Answer:**
```javascript
class Calculator {
  constructor(value = 0) {
    this.value = value;
  }

  add(num) {
    this.value += num;
    return this; // Return this for chaining
  }

  subtract(num) {
    this.value -= num;
    return this;
  }

  multiply(num) {
    this.value *= num;
    return this;
  }

  divide(num) {
    if (num === 0) {
      throw new Error('Cannot divide by zero');
    }
    this.value /= num;
    return this;
  }

  result() {
    return this.value;
  }

  reset() {
    this.value = 0;
    return this;
  }
}

let calc = new Calculator(10);
let finalValue = calc.add(5).multiply(2).subtract(10).divide(2).result();
console.log(finalValue); // 10

// (10 + 5) * 2 - 10 / 2 = 15 * 2 - 10 / 2 = 30 - 10 / 2 = 20 / 2 = 10
```

### 18. Static Properties and Counters
**Question:** Create a `User` class that tracks the total number of users created using a static property. Include a static method to get the count and an instance method that returns the user's ID (assigned sequentially).

**Answer:**
```javascript
class User {
  static #count = 0;
  static #allUsers = [];

  constructor(name) {
    this.name = name;
    this.id = ++User.#count;
    User.#allUsers.push(this);
  }

  static getUserCount() {
    return User.#count;
  }

  static getAllUsers() {
    return User.#allUsers.map(user => ({
      id: user.id,
      name: user.name
    }));
  }

  static resetCount() {
    User.#count = 0;
    User.#allUsers = [];
  }

  getInfo() {
    return `User #${this.id}: ${this.name}`;
  }
}

let user1 = new User('Alice');
let user2 = new User('Bob');
let user3 = new User('Charlie');

console.log(user1.getInfo()); // User #1: Alice
console.log(user2.getInfo()); // User #2: Bob
console.log(User.getUserCount()); // 3
console.log(User.getAllUsers());
// [
//   { id: 1, name: 'Alice' },
//   { id: 2, name: 'Bob' },
//   { id: 3, name: 'Charlie' }
// ]
```

### 19. Mixins and Composition
**Question:** Create a mixin pattern that allows you to add `canSwim` and `canFly` abilities to different animal classes without using inheritance.

**Answer:**
```javascript
// Mixin functions
const canSwim = {
  swim() {
    return `${this.name} is swimming`;
  }
};

const canFly = {
  fly() {
    return `${this.name} is flying`;
  }
};

// Base class
class Animal {
  constructor(name) {
    this.name = name;
  }
}

// Helper function to apply mixins
function mixin(targetClass, ...mixins) {
  mixins.forEach(mixin => {
    Object.assign(targetClass.prototype, mixin);
  });
}

// Create specific animal classes
class Duck extends Animal {}
class Fish extends Animal {}
class Bird extends Animal {}

// Apply mixins
mixin(Duck, canSwim, canFly);
mixin(Fish, canSwim);
mixin(Bird, canFly);

// Test
let duck = new Duck('Donald');
console.log(duck.swim()); // Donald is swimming
console.log(duck.fly()); // Donald is flying

let fish = new Fish('Nemo');
console.log(fish.swim()); // Nemo is swimming
// console.log(fish.fly()); // TypeError: fish.fly is not a function

let bird = new Bird('Tweety');
console.log(bird.fly()); // Tweety is flying
// console.log(bird.swim()); // TypeError: bird.swim is not a function
```

### 20. The 'new' Keyword Deep Dive
**Question:** What exactly happens when you use the `new` keyword? Write a function `myNew` that mimics the behavior of the `new` keyword.

**Answer:**

When you use `new`, the following happens:
1. A new empty object is created
2. The new object's `[[Prototype]]` is set to the constructor's `prototype` property
3. The constructor function is called with `this` bound to the new object
4. If the constructor returns an object, that object is returned; otherwise, the new object is returned

```javascript
function myNew(constructor, ...args) {
  // 1. Create a new object with the constructor's prototype
  const obj = Object.create(constructor.prototype);
  
  // 2. Call the constructor with the new object as 'this'
  const result = constructor.apply(obj, args);
  
  // 3. Return the result if it's an object, otherwise return the new object
  return (typeof result === 'object' && result !== null) ? result : obj;
}

// Test with a simple constructor
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.greet = function() {
  return `Hi, I'm ${this.name}`;
};

// Using regular new
let person1 = new Person('Alice', 30);
console.log(person1.greet()); // Hi, I'm Alice

// Using our myNew
let person2 = myNew(Person, 'Bob', 25);
console.log(person2.greet()); // Hi, I'm Bob

console.log(person1 instanceof Person); // true
console.log(person2 instanceof Person); // true
```

### 21. Getters and Setters
**Question:** Create a `Temperature` class that stores temperature in Celsius but allows getting and setting values in both Celsius and Fahrenheit using getters and setters.

**Answer:**
```javascript
class Temperature {
  constructor(celsius = 0) {
    this._celsius = celsius;
  }

  // Celsius getter and setter
  get celsius() {
    return this._celsius;
  }

  set celsius(value) {
    if (typeof value !== 'number') {
      throw new Error('Temperature must be a number');
    }
    this._celsius = value;
  }

  // Fahrenheit getter and setter
  get fahrenheit() {
    return (this._celsius * 9/5) + 32;
  }

  set fahrenheit(value) {
    if (typeof value !== 'number') {
      throw new Error('Temperature must be a number');
    }
    this._celsius = (value - 32) * 5/9;
  }

  // Kelvin getter and setter
  get kelvin() {
    return this._celsius + 273.15;
  }

  set kelvin(value) {
    if (typeof value !== 'number') {
      throw new Error('Temperature must be a number');
    }
    this._celsius = value - 273.15;
  }
}

let temp = new Temperature(0);
console.log(temp.celsius); // 0
console.log(temp.fahrenheit); // 32
console.log(temp.kelvin); // 273.15

temp.fahrenheit = 68;
console.log(temp.celsius); // 20
console.log(temp.kelvin); // 293.15

temp.kelvin = 300;
console.log(temp.celsius); // 26.849999999999994
console.log(temp.fahrenheit); // 80.33
```

### 22. Abstract Classes Pattern
**Question:** JavaScript doesn't have built-in abstract classes, but you can simulate them. Create an abstract `Shape` class that throws an error if instantiated directly or if required methods aren't implemented by subclasses.

**Answer:**
```javascript
class Shape {
  constructor() {
    if (new.target === Shape) {
      throw new Error('Cannot instantiate abstract class Shape directly');
    }
  }

  // Abstract method - must be overridden
  getArea() {
    throw new Error('Method getArea() must be implemented');
  }

  // Abstract method - must be overridden
  getPerimeter() {
    throw new Error('Method getPerimeter() must be implemented');
  }

  // Concrete method - can be used as-is
  describe() {
    return `This shape has an area of ${this.getArea()} and perimeter of ${this.getPerimeter()}`;
  }
}

class Circle extends Shape {
  constructor(radius) {
    super();
    this.radius = radius;
  }

  getArea() {
    return Math.PI * this.radius ** 2;
  }

  getPerimeter() {
    return 2 * Math.PI * this.radius;
  }
}

class Rectangle extends Shape {
  constructor(width, height) {
    super();
    this.width = width;
    this.height = height;
  }

  getArea() {
    return this.width * this.height;
  }

  // Oops! Forgot to implement getPerimeter()
}

// This will throw an error
// let shape = new Shape(); // Error: Cannot instantiate abstract class Shape directly

let circle = new Circle(5);
console.log(circle.describe());
// This shape has an area of 78.53981633974483 and perimeter of 31.41592653589793

let rect = new Rectangle(4, 6);
console.log(rect.getArea()); // 24
// console.log(rect.getPerimeter()); // Error: Method getPerimeter() must be implemented
// console.log(rect.describe()); // Will also throw error when it tries to call getPerimeter()
```

### 23. Class vs Constructor Function Performance
**Question:** What are the key differences between ES6 classes and constructor functions in terms of behavior and constraints?

**Answer:**

**Key Differences:**

1. **Hoisting**: Constructor functions are hoisted, classes are not
```javascript
// This works - function hoisting
let obj1 = new MyFunction();
function MyFunction() {}

// This throws ReferenceError - class not hoisted
// let obj2 = new MyClass(); // Error!
class MyClass {}
```

2. **Strict Mode**: Class bodies automatically run in strict mode
```javascript
function OldStyle() {
  // Not strict mode by default
  nonDeclaredVariable = 'oops'; // Creates global variable (bad!)
}

class NewStyle {
  constructor() {
    // Always strict mode
    // nonDeclaredVariable = 'oops'; // ReferenceError!
  }
}
```

3. **Calling Without 'new'**: Classes must be called with `new`
```javascript
function OldStyle() {
  this.value = 42;
}
OldStyle(); // Works (but this is undefined in strict mode)

class NewStyle {
  constructor() {
    this.value = 42;
  }
}
// NewStyle(); // TypeError: Class constructor NewStyle cannot be invoked without 'new'
```

4. **Method Enumeration**: Class methods are non-enumerable by default
```javascript
function OldStyle() {}
OldStyle.prototype.method = function() {};

class NewStyle {
  method() {}
}

console.log(Object.keys(OldStyle.prototype)); // ['method']
console.log(Object.keys(NewStyle.prototype)); // []
```

5. **super**: Only available in classes
```javascript
// Classes have super
class Parent {
  greet() { return 'Hello'; }
}
class Child extends Parent {
  greet() { return super.greet() + ' World'; }
}

// Constructor functions need manual prototype manipulation
function OldParent() {}
OldParent.prototype.greet = function() { return 'Hello'; };

function OldChild() {}
OldChild.prototype = Object.create(OldParent.prototype);
OldChild.prototype.constructor = OldChild;
// No clean way to call parent method
```

### 24. Memory and Performance
**Question:** Explain the difference in memory usage between defining methods inside the constructor versus on the prototype. Provide examples.

**Answer:**

**Methods in Constructor:**
- Each instance gets its own copy of the function
- Higher memory usage with many instances
- Functions are not shared

**Methods on Prototype:**
- All instances share the same function
- Lower memory usage
- Functions are delegated through prototype chain

```javascript
// BAD: Method in constructor
class BadPractice {
  constructor(name) {
    this.name = name;
    
    // New function created for EACH instance
    this.greet = function() {
      return `Hello, I'm ${this.name}`;
    };
  }
}

// GOOD: Method on prototype
class GoodPractice {
  constructor(name) {
    this.name = name;
  }
  
  // Single function shared by ALL instances
  greet() {
    return `Hello, I'm ${this.name}`;
  }
}

// Demonstration
let bad1 = new BadPractice('Alice');
let bad2 = new BadPractice('Bob');
console.log(bad1.greet === bad2.greet); // false - different functions!

let good1 = new GoodPractice('Alice');
let good2 = new GoodPractice('Bob');
console.log(good1.greet === good2.greet); // true - same function!

// Memory impact with 1000 instances:
// BadPractice: 1000 separate greet functions in memory
// GoodPractice: 1 greet function shared by all 1000 instances
```

**When to use methods in constructor:**
- When you need closure over constructor variables
- When each instance needs a truly unique function

```javascript
class Counter {
  constructor() {
    let count = 0; // Private variable in closure
    
    this.increment = function() {
      count++;
      return count;
    };
    
    this.getCount = function() {
      return count;
    };
  }
}

let counter1 = new Counter();
let counter2 = new Counter();

console.log(counter1.increment()); // 1
console.log(counter1.increment()); // 2
console.log(counter2.increment()); // 1 (separate counter)
```

### 25. Prototype Chain Manipulation
**Question:** Create a `create` function that demonstrates deep understanding of prototypes by creating an object that inherits from a specific prototype without using `class` or `new`.

**Answer:**
```javascript
// Custom create function
function create(proto, properties = {}) {
  // Create object with specified prototype
  const obj = Object.create(proto);
  
  // Add properties
  Object.keys(properties).forEach(key => {
    obj[key] = properties[key];
  });
  
  return obj;
}

// Example usage
const animalMethods = {
  eat() {
    return `${this.name} is eating`;
  },
  sleep() {
    return `${this.name} is sleeping`;
  }
};

const dogMethods = create(animalMethods, {
  bark() {
    return `${this.name} says woof!`;
  }
});

const myDog = create(dogMethods, {
  name: 'Buddy',
  breed: 'Golden Retriever'
});

console.log(myDog.name); // Buddy
console.log(myDog.bark()); // Buddy says woof!
console.log(myDog.eat()); // Buddy is eating

// Verify prototype chain
console.log(Object.getPrototypeOf(myDog) === dogMethods); // true
console.log(Object.getPrototypeOf(dogMethods) === animalMethods); // true

// Prototype chain: myDog -> dogMethods -> animalMethods -> Object.prototype -> null
```

---

## Bonus: Common Pitfalls and Best Practices

### Pitfall 1: Forgetting 'this' binding
```javascript
class Counter {
  constructor() {
    this.count = 0;
  }

  increment() {
    this.count++;
  }
}

const counter = new Counter();
const incrementFn = counter.increment;
// incrementFn(); // TypeError: Cannot read property 'count' of undefined

// Solution 1: Bind in constructor
class CounterFixed1 {
  constructor() {
    this.count = 0;
    this.increment = this.increment.bind(this);
  }
  increment() {
    this.count++;
  }
}

// Solution 2: Arrow function
class CounterFixed2 {
  count = 0;
  
  increment = () => {
    this.count++;
  }
}
```

### Pitfall 2: Modifying the prototype after instances are created
```javascript
class Dog {
  bark() {
    return 'Woof!';
  }
}

const dog1 = new Dog();
console.log(dog1.bark()); // Woof!

// Modifying prototype affects ALL instances, even existing ones
Dog.prototype.bark = function() {
  return 'Meow!';
};

console.log(dog1.bark()); // Meow! (changed!)
```