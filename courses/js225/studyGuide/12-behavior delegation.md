# JavaScript Object Creation Patterns - Questions & Answers

## Original Questions with Answers

### 1. Advanced: Write a `delegate` function

**Question:**
Write a `delegate` function that can be used to delegate the behavior of a method or function to another object's method. `delegate` takes a minimum of two arguments: (1) the object and (2) name of the method on the object. The remaining arguments, if any, are passed — as arguments — to the objects' method that it delegates to. The `delegate` function should return the same value returned by calling the other object's method.

```javascript
const foo = {
  name: 'test',
  bar(greeting) {
    console.log(`${greeting} ${this.name}`);
  },
};

const baz = {
  qux: delegate(foo, 'bar', 'hello'),
};

baz.qux();   // logs 'hello test';

foo.bar = () => { console.log('changed'); };

baz.qux();   // logs 'changed'
```

**Answer:**
```javascript
function delegate(object, methodName, ...fixedArgs) {
  return function(...additionalArgs) {
    let args = fixedArgs.concat(additionalArgs);
    return object[methodName].apply(object, args);
  };
}
```

**Explanation:**
- The function returns a new function that, when called, looks up the method on the original object by name
- Uses `apply` to call the method with the object as context
- Combines fixed arguments (passed to `delegate`) with any additional arguments passed at call time
- Maintains the reference by looking up `object[methodName]` each time, so changes to the method are reflected

---

### 2. Basic: Prototypal Inheritance Lookup

**Question:**
```javascript
let foo = {};
let bar = Object.create(foo);

foo.a = 1;

console.log(bar.a);
```

**Answer:**
Logs `1`

**Explanation:**
- `bar` is created with `foo` as its prototype
- When we access `bar.a`, JavaScript looks for the property on `bar` first
- Since `bar` doesn't have its own `a` property, it delegates to its prototype (`foo`)
- `foo.a` is `1`, so that value is returned

---

### 3. Basic: Own Property vs Inherited Property

**Question:**
```javascript
let foo = {};
let bar = Object.create(foo);

foo.a = 1;
bar.a = 2;
console.log(bar.a);
```

**Answer:**
Logs `2`

**Explanation:**
- `bar` is created with `foo` as its prototype
- `foo.a = 1` sets a property on the prototype
- `bar.a = 2` creates an **own property** on `bar`
- When accessing `bar.a`, JavaScript finds the property directly on `bar` and returns `2`
- Own properties **shadow** inherited properties with the same name

---

### 4. Intermediate: Testing Property Ownership

**Question:**
Given the code below, do we know for certain that on the last line we are ultimately referencing a property owned by `boo`? How can we test that `far` is not delegating to `boo`?

```javascript
let boo = {};
boo.myProp = 1;

let far = Object.create(boo);

// lots of code

far.myProp;       // 1
```

**Answer:**
No, we don't know for certain. The property could be owned by `far` or inherited from `boo`.

**Testing methods:**
```javascript
// Method 1: hasOwnProperty
far.hasOwnProperty('myProp');  // false if delegating, true if own property

// Method 2: Object.hasOwn (modern approach)
Object.hasOwn(far, 'myProp');  // false if delegating, true if own property

// Method 3: getOwnPropertyNames
Object.getOwnPropertyNames(far).includes('myProp'); // false if delegating
```

---

### 5. Intermediate: Implement `createObject`

**Question:**
Without using `Object.create`, create a function `createObject` that acts like it.

**Answer:**
```javascript
function createObject(obj) {
  function F() {}
  F.prototype = obj;
  return new F();
}

let foo = {
  a: 1
};

let bar = createObject(foo);
foo.isPrototypeOf(bar);         // true
```

**Explanation:**
- Creates a temporary constructor function `F`
- Sets `F.prototype` to the object we want as the prototype
- Returns a new instance of `F`, which will have `obj` as its prototype
- This is the classic pattern used before `Object.create` was introduced

---

### 6. Intermediate: Implement `begetObject` method

**Question:**
Similar to the problem above, without using `Object.create`, create a `begetObject` method that you can call on any object to create an object inherited from it.

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
foo.isPrototypeOf(bar);         // true
```

**Explanation:**
- Adds a method to `Object.prototype` so all objects inherit it
- Uses `this` to refer to the object the method is called on
- Creates and returns a new object with `this` as its prototype

---

### 7. Advanced: Implement the `new` operator

**Question:**
Create a function `neww`, so that it works like the `new` operator.

**Answer:**
```javascript
function neww(constructor, args) {
  let object = Object.create(constructor.prototype);
  let result = constructor.apply(object, args);
  
  return (typeof result === 'object' && result !== null) ? result : object;
}

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

**Explanation:**
1. Create a new object with the constructor's prototype
2. Call the constructor with the new object as `this`
3. If the constructor returns an object, use that; otherwise, return the created object
4. This handles edge cases where constructors explicitly return objects

---

### 8. Intermediate: Prototype Reassignment Timing

**Question:**
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
**TypeError: ninja.swingSword is not a function**

**Explanation:**
- When `ninja` is created, it gets a reference to the **original** `Ninja.prototype` object
- Reassigning `Ninja.prototype` creates a **new prototype object**
- `ninja` still points to the old prototype, which doesn't have `swingSword`
- Objects maintain their prototype link at creation time; it's not dynamically updated

**Fix:**
Add the method to the prototype before creating instances, or add it to the existing prototype:
```javascript
Ninja.prototype.swingSword = function() {
  return this.swung;
};
```

---

### 9. Basic: Add Method to Prototype

**Question:**
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

**Explanation:**
- Method sets `swung` to `true` on the calling object
- Returns `this` to enable method chaining
- Both instances share the same prototype method but operate on their own `swung` property

---

### 10. Advanced: Create Instance Without Direct Constructor Access

**Question:**
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
// Method 1: Using Object.create
let ninjaB = Object.create(ninjaA.constructor.prototype);

// Method 2: Using the constructor property
let ninjaB = new ninjaA.constructor();
```

**Explanation:**
- Every instance has a `constructor` property that references