# JavaScript Object Creation Patterns - Exercises & Answers

## Question 1: OLOO to Pseudo-Classical Pattern (Intermediate)

### Problem
Convert the following code from the OLOO pattern to use the pseudo-classical object creation pattern using a `Pet` constructor.

The OLOO `PetPrototype` is defined as:

```javascript
const PetPrototype = {
  init(animal, name) {
    this.animal = animal;
    this.name = name;
    return this;
  },

  sleep: function() {
    console.log("I am sleeping");
  },

  wake: function() {
    console.log("I am awake");
  },
};
```

You should be able to use the new `Pet` constructor like this:

```javascript
let pudding = new Pet("Cat", "Pudding");
console.log(`I am a ${pudding.animal}. My name is ${pudding.name}.`);
pudding.sleep(); // I am sleeping
pudding.wake();  // I am awake

let neptune = new Pet("Fish", "Neptune");
console.log(`I am a ${neptune.animal}. My name is ${neptune.name}.`);
neptune.sleep(); // I am sleeping
neptune.wake();  // I am awake
```

### Answer

```javascript
function Pet(animal, name) {
  this.animal = animal;
  this.name = name;
}

Pet.prototype.sleep = function() {
  console.log("I am sleeping");
};

Pet.prototype.wake = function() {
  console.log("I am awake");
};
```

### Explanation
- The `init` method from OLOO becomes the constructor function `Pet`
- Properties are initialized directly in the constructor using `this`
- Methods are added to `Pet.prototype` instead of being part of the prototype object
- No need to return `this` in the constructor (happens automatically with `new`)

---

## Question 2: Class Hierarchy Implementation (Advanced)

### Problem
Implement the following diagram using the pseudo-classical approach. Subclasses should inherit all of the superclass's methods. Reuse the constructors of the superclass when implementing a subclass.

### Sample Run

```javascript
const person = new Person('Foo', 'Bar', 21, 'male');
console.log(person instanceof Person);       // logs true
console.log(person instanceof Doctor);       // logs false
console.log(person instanceof Professor);    // logs false
console.log(person instanceof Student);      // logs false
person.eat();                                // logs 'Eating'
person.communicate();                        // logs 'Communicating'
person.sleep();                              // logs 'Sleeping'
console.log(person.fullName());              // logs 'Foo Bar'

const doctor = new Doctor('Bar', 'Qux', 21, 'female', 'Pediatrics');
console.log(doctor instanceof Person);       // logs true
console.log(doctor instanceof Doctor);       // logs true
console.log(doctor instanceof Professor);    // logs false
console.log(doctor instanceof Student);      // logs false
doctor.eat();                                // logs 'Eating'
doctor.communicate();                        // logs 'Communicating'
doctor.sleep();                              // logs 'Sleeping'
console.log(doctor.fullName());              // logs 'Bar Qux'
doctor.diagnose();                           // logs 'Diagnosing'

const professor = new Professor('Bar', 'Foo', 48, 'female', 'Law');
console.log(professor instanceof Person);    // logs true
console.log(professor instanceof Professor); // logs true
console.log(professor instanceof Doctor);    // logs false
console.log(professor instanceof Student);   // logs false
professor.eat();                             // logs 'Eating'
professor.communicate();                     // logs 'Communicating'
professor.sleep();                           // logs 'Sleeping'
console.log(professor.fullName());           // logs 'Bar Foo'
professor.teach();                           // logs 'Teaching'
```

### Answer

```javascript
// Base constructor
function Person(firstName, lastName, age, gender) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.age = age;
  this.gender = gender;
}

Person.prototype.eat = function() {
  console.log('Eating');
};

Person.prototype.communicate = function() {
  console.log('Communicating');
};

Person.prototype.sleep = function() {
  console.log('Sleeping');
};

Person.prototype.fullName = function() {
  return `${this.firstName} ${this.lastName}`;
};

// Doctor constructor
function Doctor(firstName, lastName, age, gender, specialization) {
  Person.call(this, firstName, lastName, age, gender);
  this.specialization = specialization;
}

Doctor.prototype = Object.create(Person.prototype);
Doctor.prototype.constructor = Doctor;

Doctor.prototype.diagnose = function() {
  console.log('Diagnosing');
};

// Professor constructor
function Professor(firstName, lastName, age, gender, subject) {
  Person.call(this, firstName, lastName, age, gender);
  this.subject = subject;
}

Professor.prototype = Object.create(Person.prototype);
Professor.prototype.constructor = Professor;

Professor.prototype.teach = function() {
  console.log('Teaching');
};

// Student constructor
function Student(firstName, lastName, age, gender, degree) {
  Person.call(this, firstName, lastName, age, gender);
  this.degree = degree;
}

Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;

Student.prototype.study = function() {
  console.log('Studying');
};
```

### Key Concepts
1. **Constructor Reuse**: Use `Person.call(this, ...)` to invoke the parent constructor
2. **Prototype Chain**: Set `Constructor.prototype = Object.create(Parent.prototype)`
3. **Constructor Property**: Reset the `constructor` property after changing the prototype
4. **Method Inheritance**: All methods from `Person.prototype` are accessible to subclasses

---

## Additional Tricky Questions

### Question 3: Prototype Chain Breaking (Intermediate)

What's wrong with the following code? Why doesn't `doctor.eat()` work?

```javascript
function Person(name) {
  this.name = name;
}

Person.prototype.eat = function() {
  console.log('Eating');
};

function Doctor(name, specialization) {
  Person.call(this, name);
  this.specialization = specialization;
}

// Incorrect inheritance setup
Doctor.prototype = Person.prototype;
Doctor.prototype.constructor = Doctor;

Doctor.prototype.diagnose = function() {
  console.log('Diagnosing');
};

const doctor = new Doctor('House', 'Diagnostics');
const person = new Person('John');

doctor.eat();    // Works, but...
person.diagnose(); // This shouldn't work but does! Why?
```

#### Answer
The problem is `Doctor.prototype = Person.prototype` makes both constructors share the same prototype object. This means:
- Any methods added to `Doctor.prototype` are also added to `Person.prototype`
- `person.diagnose()` works because `Person.prototype` now has the `diagnose` method
- This violates encapsulation and proper inheritance

**Correct approach:**
```javascript
Doctor.prototype = Object.create(Person.prototype);
Doctor.prototype.constructor = Doctor;
```

---

### Question 4: Constructor Property Mystery (Advanced)

Examine this code and answer the questions:

```javascript
function Animal(name) {
  this.name = name;
}

function Dog(name, breed) {
  Animal.call(this, name);
  this.breed = breed;
}

Dog.prototype = Object.create(Animal.prototype);
// Notice: we forgot to reset the constructor!

const fido = new Dog('Fido', 'Labrador');

console.log(fido.constructor === Dog);     // What does this log?
console.log(fido.constructor === Animal);  // What does this log?
console.log(fido instanceof Dog);          // What does this log?
console.log(fido instanceof Animal);       // What does this log?

const newDog = new fido.constructor('Buddy', 'Beagle');
console.log(newDog instanceof Dog);        // What does this log?
```

#### Answer
```javascript
console.log(fido.constructor === Dog);     // false
console.log(fido.constructor === Animal);  // true
console.log(fido instanceof Dog);          // true
console.log(fido instanceof Animal);       // true

const newDog = new fido.constructor('Buddy', 'Beagle');
console.log(newDog instanceof Dog);        // false (it's an Animal!)
```

**Explanation:**
- `fido.constructor` points to `Animal` because we didn't reset it after `Object.create()`
- `instanceof` still works correctly because it checks the prototype chain, not the constructor property
- Creating a new object with `fido.constructor` creates an `Animal`, not a `Dog`
- This is why resetting the constructor property is important: `Dog.prototype.constructor = Dog;`

---

### Question 5: Method Override Challenge (Advanced)

What will the following code output? Explain why.

```javascript
function Vehicle(type) {
  this.type = type;
}

Vehicle.prototype.move = function() {
  console.log(`${this.type} is moving`);
};

function Car(brand) {
  Vehicle.call(this, 'Car');
  this.brand = brand;
}

Car.prototype = Object.create(Vehicle.prototype);
Car.prototype.constructor = Car;

Car.prototype.move = function() {
  console.log(`${this.brand} car is driving`);
};

function Tesla(model) {
  Car.call(this, 'Tesla');
  this.model = model;
  this.move = function() {
    console.log(`Tesla ${this.model} is accelerating silently`);
  };
}

Tesla.prototype = Object.create(Car.prototype);
Tesla.prototype.constructor = Tesla;

const myTesla = new Tesla('Model 3');
myTesla.move();

delete myTesla.move;
myTesla.move();
```

#### Answer
```javascript
myTesla.move(); // "Tesla Model 3 is accelerating silently"
delete myTesla.move;
myTesla.move(); // "Tesla car is driving"
```

**Explanation:**
- First call uses the instance method (defined directly on the object in the constructor)
- After deletion, JavaScript looks up the prototype chain and finds `Car.prototype.move`
- The method resolution order is: instance properties → prototype chain
- Instance methods shadow prototype methods with the same name

---

### Question 6: This Binding Trap (Intermediate)

What's the problem with this code and how do you fix it?

```javascript
function Counter(count) {
  this.count = count || 0;
}

Counter.prototype.increment = function() {
  this.count++;
  console.log(this.count);
};

const counter = new Counter(5);
counter.increment(); // 6

const incrementFunc = counter.increment;
incrementFunc(); // What happens here?

setTimeout(counter.increment, 1000); // What about here?
```

#### Answer
Both `incrementFunc()` and `setTimeout(counter.increment, 1000)` will either throw an error or not work as expected because `this` is not bound to the `counter` object.

**Solutions:**

```javascript
// Solution 1: bind
const incrementFunc = counter.increment.bind(counter);
incrementFunc(); // Works!

setTimeout(counter.increment.bind(counter), 1000); // Works!

// Solution 2: arrow function wrapper
setTimeout(() => counter.increment(), 1000); // Works!

// Solution 3: Store reference
const self = counter;
setTimeout(function() { self.increment(); }, 1000); // Works!
```

---

### Question 7: Prototype Pollution (Advanced)

What's dangerous about this code? What would you change?

```javascript
function User(name) {
  this.name = name;
}

User.prototype.role = 'guest'; // Default role

const admin = new User('Admin');
admin.role = 'admin';

const user1 = new User('Alice');
const user2 = new User('Bob');

console.log(user1.role); // 'guest'
console.log(user2.role); // 'guest'

// Later in the code...
delete admin.role;
admin.role = 'superadmin';

// Somewhere else...
User.prototype.role = 'banned';

console.log(user1.role); // What does this log?
console.log(user2.role); // What does this log?
console.log(admin.role); // What does this log?
```

#### Answer
```javascript
console.log(user1.role); // 'banned'
console.log(user2.role); // 'banned'
console.log(admin.role); // 'superadmin'
```

**Problem:** Modifying `User.prototype.role` affects all instances that don't have their own `role` property.

**Better approach:**
```javascript
function User(name, role) {
  this.name = name;
  this.role = role || 'guest'; // Set in constructor, not prototype
}
```

This ensures each instance has its own `role` property, preventing prototype pollution.

---

### Question 8: Multiple Inheritance Attempt (Advanced)

A developer tries to implement multiple inheritance. What's wrong and how would you solve it properly?

```javascript
function CanSwim() {}
CanSwim.prototype.swim = function() {
  console.log('Swimming');
};

function CanFly() {}
CanFly.prototype.fly = function() {
  console.log('Flying');
};

function Duck(name) {
  this.name = name;
}

// Attempting multiple inheritance
Duck.prototype = Object.create(CanSwim.prototype);
Duck.prototype = Object.create(CanFly.prototype); // This overwrites the previous line!

const donald = new Duck('Donald');
donald.swim(); // Error!
donald.fly();  // Works
```

#### Answer
The second `Object.create()` completely replaces the first one, so `Duck` only inherits from `CanFly`.

**Solution using mixins:**
```javascript
function CanSwim() {}
CanSwim.prototype.swim = function() {
  console.log('Swimming');
};

function CanFly() {}
CanFly.prototype.fly = function() {
  console.log('Flying');
};

function Duck(name) {
  this.name = name;
}

// Copy methods from multiple sources
Object.assign(Duck.prototype, CanSwim.prototype, CanFly.prototype);

const donald = new Duck('Donald');
donald.swim(); // Swimming
donald.fly();  // Flying
```

Alternatively, use composition or ES6 classes with mixins for a more robust solution.