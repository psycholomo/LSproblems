# JavaScript Constructor Functions - Questions & Answers

## Original Questions

### 1. Basic: What naming convention separates constructor functions from other functions?

**Answer:** Constructor functions use **PascalCase** (also called UpperCamelCase), where the first letter is capitalized. Regular functions use **camelCase** with a lowercase first letter.

Examples:
- Constructor: `function Person() {}`
- Regular function: `function createPerson() {}`

---

### 2. Intermediate: What will the code below output? Why?

```javascript
function Lizard() {
  this.scamper = function() {
    console.log("I'm scampering!");
  };
}

let lizzy = Lizard();
lizzy.scamper(); // ?
```

**Answer:** This code will throw a **TypeError: Cannot read property 'scamper' of undefined**.

**Why?** When `Lizard()` is called without the `new` operator, `this` refers to the global object (or `undefined` in strict mode). The function doesn't explicitly return anything, so `lizzy` is `undefined`. You cannot call a method on `undefined`.

---

### 3. Intermediate: Alter the code in the previous problem so that it produces the desired output.

**Answer:**
```javascript
function Lizard() {
  this.scamper = function() {
    console.log("I'm scampering!");
  };
}

let lizzy = new Lizard(); // Add 'new' keyword
lizzy.scamper(); // "I'm scampering!"
```

---

### 4. Intermediate: Write a constructor function Circle

**Answer:**
```javascript
function Circle(radius) {
  this.radius = radius;
}

Circle.prototype.area = function() {
  return Math.PI * this.radius * this.radius;
};

// Test
let a = new Circle(3);
let b = new Circle(4);

console.log(a.area().toFixed(2)); // => 28.27
console.log(b.area().toFixed(2)); // => 50.27
```

---

### 5. Intermediate: What will the following code log out and why?

```javascript
let ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja();

Ninja.prototype.swingSword = function() {
  return this.swung;
};

console.log(ninja.swingSword());
```

**Answer:** This will log `true`.

**Why?** Even though `swingSword` is added to the prototype after the `ninja` object is created, JavaScript uses prototype chain lookup at the time of method invocation. When `ninja.swingSword()` is called, JavaScript looks up the prototype chain and finds the method on `Ninja.prototype`, which can then access `this.swung` (which is `true`).

---

### 6. Intermediate: Update the following code to log constructor names

**Answer:**
```javascript
console.log("Hello".constructor.name);        // String
console.log([1,2,3].constructor.name);        // Array
console.log({name: 'Srdjan'}.constructor.name); // Object
```

---

### 7. Advanced: What will the following code log out and why?

```javascript
let ninja;
function Ninja() {
  this.swung = true;
}

ninja = new Ninja();

Ninja.prototype = {
  swingSword: function() {
    return this.swung;
  },
};

console.log(ninja.swingSword());
```

**Answer:** This will throw a **TypeError: ninja.swingSword is not a function**.

**Why?** When `ninja` is created with `new Ninja()`, it gets a reference to the original `Ninja.prototype` object. After that, we reassign `Ninja.prototype` to a completely new object. However, `ninja` still points to the old prototype object, which doesn't have the `swingSword` method. The reassignment doesn't affect already-created instances.

---

### 8. Advanced: Create shape object and Triangle constructor

**Answer:**
```javascript
let shape = {
  getType: function() {
    return this.type;
  }
};

function Triangle(a, b, c) {
  this.a = a;
  this.b = b;
  this.c = c;
  this.type = 'triangle';
}

Triangle.prototype = shape;
Triangle.prototype.constructor = Triangle;

Triangle.prototype.getPerimeter = function() {
  return this.a + this.b + this.c;
};

// Test
let t = new Triangle(3, 4, 5);
t.constructor;                 // Triangle(a, b, c)
shape.isPrototypeOf(t);        // true
t.getPerimeter();              // 12
t.getType();                   // "triangle"
```

---

### 9. Advanced: Constructor that works with or without 'new'

**Answer:**
```javascript
function User(first, last) {
  if (!(this instanceof User)) {
    return new User(first, last);
  }
  
  this.name = first + ' ' + last;
}

// Test
let name = 'Jane Doe';
let user1 = new User('John', 'Doe');
let user2 = User('John', 'Doe');

console.log(name);         // => Jane Doe
console.log(user1.name);   // => John Doe
console.log(user2.name);   // => John Doe
```

---

### 10. Advanced: Create Object.create alternative

**Answer:**
```javascript
function createObject(obj) {
  function F() {}
  F.prototype = obj;
  return new F();
}

// Test
let foo = {
  a: 1
};

let bar = createObject(foo);
foo.isPrototypeOf(bar);         // true
```

---

### 11. Advanced: Create begetObject method

**Answer:**
```javascript
Object.prototype.begetObject = function() {
  function F() {}
  F.prototype = this;
  return new F();
};

// Test
let foo = {
  a: 1,
};

let bar = foo.begetObject();
foo.isPrototypeOf(bar);         // true
```

---

### 12. Advanced: Implement 'new' operator

**Answer:**
```javascript
function neww(constructor, args) {
  let obj = Object.create(constructor.prototype);
  let result = constructor.apply(obj, args);
  return (typeof result === 'object' && result !== null) ? result : obj;
}

// Test
function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
}

Person.prototype.greeting = function() {
  console.log('Hello, ' + this.firstName + ' ' + this.lastName);
};

let john = neww(Person, ['John', 'Doe']);
john.greeting();          // => Hello, John Doe
john.constructor;         // Person(firstName, lastName) {...}
```

---

## Additional Tricky Questions

### 13. Advanced: Prototype Chain Mystery

What will this code output and why?

```javascript
function Animal(name) {
  this.name = name;
}

Animal.prototype.speak = function() {
  return `${this.name} makes a sound`;
};

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);

let buddy = new Dog('Buddy', 'Golden Retriever');

console.log(buddy.constructor.name);
console.log(buddy instanceof Dog);
console.log(buddy instanceof Animal);
```

**Answer:**
- `"Animal"` - The constructor property wasn't reset after setting the prototype
- `true` - buddy is an instance of Dog
- `true` - buddy is also an instance of Animal through the prototype chain

To fix the constructor, add: `Dog.prototype.constructor = Dog;`

---

### 14. Advanced: Return Value Confusion

What will each of these constructors return?

```javascript
function A() {
  this.value = 1;
  return { value: 2 };
}

function B() {
  this.value = 1;
  return 'string';
}

function C() {
  this.value = 1;
  return null;
}

let a = new A();
let b = new B();
let c = new C();

console.log(a.value); // ?
console.log(b.value); // ?
console.log(c.value); // ?
```

**Answer:**
- `a.value` → `2` (object return value overrides)
- `b.value` → `1` (primitive return values are ignored)
- `c.value` → `1` (null is a special case, treated as no return)

---

### 15. Expert: Prototype Pollution

What's the issue with this code and how would you fix it?

```javascript
function User(name) {
  this.name = name;
  this.friends = [];
}

User.prototype.friends = [];

User.prototype.addFriend = function(friend) {
  this.friends.push(friend);
};

let user1 = new User('Alice');
let user2 = new User('Bob');

user1.addFriend('Charlie');

console.log(user1.friends); // ?
console.log(user2.friends); // ?
```

**Answer:** Both will show `['Charlie']` because if an instance doesn't have its own `friends` property, it will use the prototype's `friends` array, which is shared.

**Fix:** Always initialize array/object properties in the constructor:
```javascript
function User(name) {
  this.name = name;
  this.friends = []; // Instance property
}
```

---

### 16. Expert: The 'this' Trap

What will this output?

```javascript
function Counter() {
  this.count = 0;
  this.increment = function() {
    this.count++;
  };
}

Counter.prototype.increment = function() {
  this.count += 10;
};

let c1 = new Counter();
let c2 = new Counter();

c1.increment();
delete c1.increment;
c1.increment();

console.log(c1.count); // ?
console.log(c2.count); // ?
```

**Answer:**
- `c1.count` → `11` (first increment adds 1, then after deletion, prototype method adds 10)
- `c2.count` → `0` (untouched)

---

### 17. Expert: Arrow Functions as Constructors

What happens when you try this?

```javascript
const Person = (name) => {
  this.name = name;
};

let john = new Person('John'); // ?
```

**Answer:** **TypeError: Person is not a constructor**

Arrow functions cannot be used as constructors and don't have their own `this` binding or `prototype` property.

---

### 18. Expert: Prototype vs Own Properties

Implement a function that counts how many properties an object has in total (both own and inherited from prototype), and how many are own properties.

```javascript
function analyzeProperties(obj) {
  // Your implementation
}

function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {};

let p = new Person('Alice');
console.log(analyzeProperties(p));
// Should return: { total: 2, own: 1 }
```

**Answer:**
```javascript
function analyzeProperties(obj) {
  let own = Object.keys(obj).length;
  let total = 0;
  
  for (let prop in obj) {
    total++;
  }
  
  return { total, own };
}
```

---

### 19. Expert: Constructor Hijacking

What security issue exists here and how would you prevent it?

```javascript
function SecureUser(username, password) {
  this.username = username;
  this.password = password;
}

// Potential issue:
SecureUser.prototype.getPassword = function() {
  return this.password;
};
```

**Answer:** The password is exposed as a public property. Use closures for true privacy:

```javascript
function SecureUser(username, password) {
  this.username = username;
  
  this.authenticate = function(pass) {
    return pass === password;
  };
  
  // password is now in closure, not accessible from outside
}
```

---

### 20. Expert: Multiple Inheritance Pattern

Implement a mixin pattern that allows an object to inherit from multiple sources:

```javascript
function mixin(target, ...sources) {
  // Your implementation
}

let canEat = {
  eat() { return 'eating'; }
};

let canWalk = {
  walk() { return 'walking'; }
};

function Person(name) {
  this.name = name;
}

mixin(Person.prototype, canEat, canWalk);

let person = new Person('John');
console.log(person.eat());  // 'eating'
console.log(person.walk()); // 'walking'
```

**Answer:**
```javascript
function mixin(target, ...sources) {
  sources.forEach(source => {
    Object.keys(source).forEach(key => {
      target[key] = source[key];
    });
  });
  return target;
}
```
