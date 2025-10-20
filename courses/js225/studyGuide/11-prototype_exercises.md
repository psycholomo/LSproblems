# JavaScript Prototype Practice Questions & Answers

## Basic Questions

### Question 1
**Difficulty: Basic**

Use the method we learned above to assign foo below to a new Object with prot as its prototype.

```javascript
let prot = {};
let foo = // ?
```

**Answer:**
```javascript
let prot = {};
let foo = Object.create(prot);
```

---

### Question 2
**Difficulty: Basic**

Use `getPrototypeOf` to demonstrate the prototypal relationship between prot and foo.

**Answer:**
```javascript
let prot = {};
let foo = Object.create(prot);

console.log(Object.getPrototypeOf(foo) === prot); // true
```

---

### Question 3
**Difficulty: Basic**

Use `isPrototypeOf` to demonstrate the prototypal relationship between prot and foo.

**Answer:**
```javascript
let prot = {};
let foo = Object.create(prot);

console.log(prot.isPrototypeOf(foo)); // true
```

---

### Question 4
**Difficulty: Basic**

What will the last two lines of the code below return? Why?

```javascript
let prot = {};
let foo = Object.create(prot);

prot.isPrototypeOf(foo);
Object.prototype.isPrototypeOf(foo);
```

**Answer:**

Both return `true`.

- `prot.isPrototypeOf(foo)` returns `true` because `prot` is the direct prototype of `foo`.
- `Object.prototype.isPrototypeOf(foo)` returns `true` because `Object.prototype` is in the prototype chain of `foo`. The chain is: `foo` → `prot` → `Object.prototype` → `null`.

---

### Question 5
**Difficulty: Basic**

What will the code below log to the console?

```javascript
let foo = {};
let bar = Object.create(foo);

foo.a = 1;

console.log(bar.a);
```

**Answer:**

It will log `1`.

When `bar.a` is accessed, JavaScript doesn't find property `a` on `bar` itself, so it looks up the prototype chain and finds `a` on `foo` with value `1`.

---

### Question 6
**Difficulty: Basic**

What will the code below log to the console?

```javascript
let foo = {};
let bar = Object.create(foo);

foo.a = 1;
bar.a = 2;
console.log(bar.a);
```

**Answer:**

It will log `2`.

Even though `foo.a` is `1`, when we assign `bar.a = 2`, we're creating an own property on `bar` that shadows the prototype property. When accessing `bar.a`, JavaScript finds the own property first and returns `2`.

---

## Intermediate Questions

### Question 7
**Difficulty: Intermediate**

Write a constructor function Circle, that takes a radius as an argument. You should be able to call an area method on the created objects to get the circle's area. Test your implementation with the following code:

```javascript
let a = new Circle(3);
let b = new Circle(4);

console.log(a.area().toFixed(2)); // => 28.27
console.log(b.area().toFixed(2)); // => 50.27
```

**Answer:**
```javascript
function Circle(radius) {
  this.radius = radius;
}

Circle.prototype.area = function() {
  return Math.PI * this.radius * this.radius;
};

let a = new Circle(3);
let b = new Circle(4);

console.log(a.area().toFixed(2)); // => 28.27
console.log(b.area().toFixed(2)); // => 50.27
```

---

### Question 8
**Difficulty: Intermediate**

What will the following code log out and why?

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

**Answer:**

It will log `true`.

Even though `swingSword` is added to `Ninja.prototype` after `ninja` is instantiated, the `ninja` object has a reference to `Ninja.prototype` through its internal `[[Prototype]]` property. When `swingSword` is called, JavaScript finds it on the prototype and executes it, returning the value of `this.swung`, which is `true`.

---

### Question 9
**Difficulty: Intermediate**

What will the following code log out and why?

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

**Answer:**

This will throw a `TypeError: ninja.swingSword is not a function`.

When `ninja` was instantiated, it received a reference to the original `Ninja.prototype` object. When we reassign `Ninja.prototype` to a new object, the `ninja` object still references the old prototype, which doesn't have a `swingSword` method. Only objects created with `new Ninja()` after the reassignment would have access to the new prototype.

---

### Question 10
**Difficulty: Intermediate**

Implement the method described in the comments below:

```javascript
let ninjaA;
let ninjaB;
function Ninja() {
  this.swung = false;
}

ninjaA = new Ninja();
ninjaB = new Ninja();

// Add a swing method to the Ninja prototype which
// returns the calling object and modifies swung

console.log(ninjaA.swing().swung);      // must log true
console.log(ninjaB.swing().swung);      // must log true
```

**Answer:**
```javascript
Ninja.prototype.swing = function() {
  this.swung = true;
  return this;
};
```

The method modifies the `swung` property on the calling object and returns `this` to enable method chaining.

---

## Advanced Questions

### Question 11
**Difficulty: Advanced**

Write a function that returns the object on a given object's prototype chain where a property is defined.

```javascript
function getDefiningObject(object, propKey) {
  // ...
}

let foo = {
  a: 1,
  b: 2,
};

let bar = Object.create(foo);
let baz = Object.create(bar);
let qux = Object.create(baz);

bar.c = 3;

console.log(getDefiningObject(qux, 'c') === bar);     // => true
console.log(getDefiningObject(qux, 'e'));             // => null
```

**Answer:**
```javascript
function getDefiningObject(object, propKey) {
  while (object) {
    if (object.hasOwnProperty(propKey)) {
      return object;
    }
    object = Object.getPrototypeOf(object);
  }
  return null;
}
```

This function walks up the prototype chain using `Object.getPrototypeOf()` and checks each object for the property using `hasOwnProperty()`. If found, it returns that object; otherwise, it returns `null`.

---

### Question 12
**Difficulty: Advanced**

Write a function to provide a shallow copy of an object. The object that you copy should share the same prototype chain as the original object, and it should have the same own properties that return the same values or objects when accessed.

```javascript
function shallowCopy(object) {
  // ...
}

let foo = {
  a: 1,
  b: 2,
};

let bar = Object.create(foo);
bar.c = 3;
bar.say = function() {
  console.log('c is ' + this.c);
};

let baz = shallowCopy(bar);
console.log(baz.a);       // => 1
baz.say();                // => c is 3
baz.hasOwnProperty('a');  // false
baz.hasOwnProperty('b');  // false
baz.hasOwnProperty('c');  // true
```

**Answer:**
```javascript
function shallowCopy(object) {
  let copy = Object.create(Object.getPrototypeOf(object));
  
  Object.getOwnPropertyNames(object).forEach(prop => {
    copy[prop] = object[prop];
  });
  
  return copy;
}
```

This creates a new object with the same prototype as the original, then copies all own properties from the original to the new object.

---

### Question 13
**Difficulty: Advanced**

Similar to the problem above, without using `Object.create`, create a `begetObject` method that you can call on any object to create an object inherited from it:

```javascript
let foo = {
  a: 1,
};

let bar = foo.begetObject();
foo.isPrototypeOf(bar);         // true
```

**Answer:**
```javascript
Object.prototype.begetObject = function() {
  function F() {}
  F.prototype = this;
  return new F();
};

let foo = {
  a: 1,
};

let bar = foo.begetObject();
console.log(foo.isPrototypeOf(bar)); // true
```

This method uses a temporary constructor function pattern to create a new object with `this` as its prototype. This is essentially what `Object.create` does internally.

---

### Question 14
**Difficulty: Advanced**

Use the OLOO (Objects Linking to Other Objects) pattern to create an object prototype that we can use to create pet objects.

```javascript
let pudding = Object.create(PetPrototype).init("Cat", "Pudding");
console.log(`I am a ${pudding.animal}. My name is ${pudding.name}.`);
pudding.sleep(); // I am sleeping
pudding.wake();  // I am awake

let neptune = Object.create(PetPrototype).init("Fish", "Neptune");
console.log(`I am a ${neptune.animal}. My name is ${neptune.name}.`);
neptune.sleep(); // I am sleeping
neptune.wake();  // I am awake
```

**Answer:**
```javascript
let PetPrototype = {
  init(animal, name) {
    this.animal = animal;
    this.name = name;
    return this;
  },
  
  sleep() {
    console.log("I am sleeping");
  },
  
  wake() {
    console.log("I am awake");
  }
};
```

The `init` method initializes the object's properties and returns `this` to allow method chaining.

---

### Question 15
**Difficulty: Advanced**

In this problem, we'll ask you to create a new instance of an object, without having direct access to the constructor function:

```javascript
let ninjaA = (function() {
  function Ninja(){};
  return new Ninja();
})();

// create a ninjaB object

console.log(ninjaB.constructor === ninjaA.constructor);    // should log true
```

**Answer:**
```javascript
let ninjaB = new ninjaA.constructor();

// Or alternatively:
let ninjaB = Object.create(Object.getPrototypeOf(ninjaA));
```

We can access the constructor through the `constructor` property on `ninjaA`, which references the `Ninja` constructor function through the prototype chain.

---

## Additional Tricky Questions

### Question 16
**Difficulty: Advanced**

What will the following code output and why?

```javascript
function Dog(name) {
  this.name = name;
}

Dog.prototype.bark = function() {
  console.log(`${this.name} says woof!`);
};

let dog1 = new Dog("Rex");
let dog2 = new Dog("Max");

dog1.bark = function() {
  console.log(`${this.name} says meow!`);
};

dog1.bark();
dog2.bark();
Dog.prototype.bark.call(dog1);
```

**Answer:**
```
Rex says meow!
Max says woof!
Rex says woof!
```

- `dog1.bark()` calls the own property method on dog1, which outputs "meow"
- `dog2.bark()` calls the prototype method, which outputs "woof"
- `Dog.prototype.bark.call(dog1)` explicitly calls the prototype method with dog1 as context, outputting "woof"

---

### Question 17
**Difficulty: Advanced**

What's wrong with this code and how would you fix it?

```javascript
function Person(name) {
  this.name = name;
  this.friends = [];
}

let alice = new Person("Alice");
let bob = new Person("Bob");

Person.prototype.friends.push("Charlie");

console.log(alice.friends); // ?
console.log(bob.friends);   // ?
```

**Answer:**

The problem is that `friends` is an own property, not a prototype property. The code tries to push to `Person.prototype.friends`, which doesn't exist (it would be `undefined`), causing an error.

If we wanted `friends` to be shared (which is usually NOT desired), we would do:
```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.friends = [];
```

But this would cause all instances to share the same array. The original implementation (with `friends` as an own property) is actually correct for most use cases.

---

### Question 18
**Difficulty: Intermediate**

Predict the output:

```javascript
let animal = {
  eats: true
};

let rabbit = Object.create(animal);

delete rabbit.eats;

console.log(rabbit.eats);
```

**Answer:**

It will output `true`.

The `delete` operator only removes own properties. Since `eats` is inherited from `animal` (not an own property of `rabbit`), the delete operation has no effect, and `rabbit.eats` still returns `true` from the prototype.

---

### Question 19
**Difficulty: Advanced**

What will this output and why?

```javascript
function A() {}
A.prototype.value = 1;

function B() {}
B.prototype = Object.create(A.prototype);
B.prototype.constructor = B;
B.prototype.value = 2;

let obj = new B();
console.log(obj.value);

delete B.prototype.value;
console.log(obj.value);
```

**Answer:**
```
2
1
```

- Initially, `obj.value` finds `value` on `B.prototype` and returns `2`
- After deleting `B.prototype.value`, the property lookup continues up the chain to `A.prototype`, where it finds `value` with the value `1`

---

### Question 20
**Difficulty: Advanced**

Fix the following code so that all objects instantiated from it lack access to the `destroy` method but maintain access to all other methods:

```javascript
function Game() {}

Game.prototype.play = function() {
  return 'Playing';
};

Game.prototype.destroy = function() {
  return 'Destroyed';
};

let game = new Game();
```

**Answer:**

There are several approaches:

**Option 1: Use a symbol**
```javascript
const DESTROY = Symbol('destroy');

function Game() {}

Game.prototype.play = function() {
  return 'Playing';
};

Game.prototype[DESTROY] = function() {
  return 'Destroyed';
};

// Can only call with: game[DESTROY]()
```

**Option 2: Use closure**
```javascript
function Game() {
  let destroyed = false;
  
  this.play = function() {
    return destroyed ? 'Cannot play' : 'Playing';
  };
  
  // Keep destroy private
  function destroy() {
    destroyed = true;
    return 'Destroyed';
  }
}
```

**Option 3: Define destroy as non-enumerable**
```javascript
function Game() {}

Game.prototype.play = function() {
  return 'Playing';
};

Object.defineProperty(Game.prototype, 'destroy', {
  value: function() {
    return 'Destroyed';
  },
  enumerable: false,
  writable: true,
  configurable: true
});
```

---

### Question 21
**Difficulty: Expert**

Implement a `deepClone` function that properly clones an object including its prototype chain:

```javascript
function deepClone(obj) {
  // Your implementation
}

let parent = { a: 1 };
let child = Object.create(parent);
child.b = { c: 2 };

let clone = deepClone(child);
console.log(clone.a); // 1 (from prototype)
console.log(clone.b.c); // 2
console.log(clone.b === child.b); // false (deep clone)
console.log(Object.getPrototypeOf(clone) === parent); // true
```

**Answer:**
```javascript
function deepClone(obj) {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }
  
  // Create new object with same prototype
  let clone = Object.create(Object.getPrototypeOf(obj));
  
  // Copy own properties recursively
  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      clone[key] = deepClone(obj[key]);
    }
  }
  
  return clone;
}
```

This function recursively clones all own properties while maintaining the prototype chain.

---

### Question 22
**Difficulty: Expert**

What's the output and explain the behavior:

```javascript
function Foo() {}
Foo.prototype.constructor = Foo;

let foo1 = new Foo();
let foo2 = new foo1.constructor();

console.log(foo1.constructor === Foo);
console.log(foo2.constructor === Foo);
console.log(foo1 instanceof Foo);
console.log(foo2 instanceof Foo);

Foo.prototype = {};
let foo3 = new Foo();

console.log(foo1.constructor === Foo);
console.log(foo3.constructor === Foo);
console.log(foo1 instanceof Foo);
console.log(foo3 instanceof Foo);
```

**Answer:**
```
true
true
true
true
true
false
false
true
```

**Explanation:**
- First four are `true` because foo1 and foo2 both reference the original prototype
- After reassigning `Foo.prototype`:
  - `foo1.constructor === Foo` is still `true` (references old prototype)
  - `foo3.constructor === Foo` is `false` (new prototype doesn't have constructor property, inherits from Object.prototype)
  - `foo1 instanceof Foo` is `false` (instanceof checks current prototype chain)
  - `foo3 instanceof Foo` is `true` (uses current prototype)

This demonstrates the difference between `constructor` (a property that can be outdated) and `instanceof` (checks the actual prototype chain).
