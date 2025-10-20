# Partial Function Application: Questions & Answers

## 1. Basic - makeSub Function

**Question:** Use partial function application to implement a function, `makeSub`, that returns a function that subtracts 5 from the argument passed to the return function.

**Answer:**
```javascript
function subtract(a, b) {
  return a - b;
}

function makeSub() {
  return function(a) {
    return subtract(a, 5);
  };
}

const sub5 = makeSub();
console.log(sub5(10)); // 5
console.log(sub5(20)); // 15
```

---

## 2. Basic - makeSubN Function

**Question:** Implement the `makeSubN` function so that we can supply any value we want to be subtracted.

**Answer:**
```javascript
function subtract(a, b) {
  return a - b;
}

function makeSubN(n) {
  return function(a) {
    return subtract(a, n);
  };
}

const sub4 = makeSubN(4);
const sub7 = makeSubN(7);
console.log(sub4(10)); // 6
console.log(sub4(20)); // 16
console.log(sub7(10)); // 3
console.log(sub7(20)); // 13
```

---

## 3. Intermediate - makePartialFunc

**Question:** Implement `makePartialFunc` to work with any operation, not just subtraction.

**Answer:**
```javascript
function makePartialFunc(func, b) {
  return function(a) {
    return func(a, b);
  };
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  return a / b;
}

let multiplyBy5 = makePartialFunc(multiply, 5);
let divideBy2 = makePartialFunc(divide, 2);
console.log(multiplyBy5(100)); // 500
console.log(divideBy2(100)); // 50
```

---

## 4. Intermediate (Conceptual) - Closures

**Question:** In the solution to the previous problem, `multiplyBy5` retains access to `func` and `b` long after `makePartialFunc` has finished execution. What makes this possible?

**Answer:**
This is made possible by **closures**. When `makePartialFunc` returns a function, that returned function maintains access to the variables in its parent scope (`func` and `b`). Even though `makePartialFunc` has finished executing, the returned function still has access to these variables through the closure mechanism. JavaScript preserves the environment in which the function was created.

---

## 5. Intermediate - greet Function

**Question:** Write a function named `greet` that takes two arguments and logs a greeting.

**Answer:**
```javascript
function greet(greeting, name) {
  let capitalized = greeting[0].toUpperCase() + greeting.slice(1);
  let message = capitalized + ', ' + name + '!';
  console.log(message);
}

greet('howdy', 'Joe');
// Howdy, Joe!

greet('good morning', 'Sue');
// Good morning, Sue!
```

---

## 6. Intermediate - sayHello and sayHi

**Question:** Use the partial function and your greet solution to create `sayHello` and `sayHi` functions.

**Answer:**
```javascript
function partial(primary, arg1) {
  return function(arg2) {
    return primary(arg1, arg2);
  };
}

function greet(greeting, name) {
  let capitalized = greeting[0].toUpperCase() + greeting.slice(1);
  let message = capitalized + ', ' + name + '!';
  console.log(message);
}

let sayHello = partial(greet, 'hello');
let sayHi = partial(greet, 'hi');

sayHello('Brandon');
// Hello, Brandon!

sayHi('Sarah');
// Hi, Sarah!
```

---

## 7. Intermediate - makeMathRollCall

**Question:** Implement `makeMathRollCall` such that it returns a partially applied `rollCall` function, with the subject as 'Math'.

**Answer:**
```javascript
let subjects = {
  English: ['Bob', 'Tyrone', 'Lizzy'],
  Math: ['Fatima', 'Gary', 'Susan'],
  Biology: ['Jack', 'Sarah', 'Tanya'],
};

function rollCall(subject, students) {
  console.log(subject + ':');
  students.forEach(function(student) {
    console.log(student);
  });
}

function makeMathRollCall() {
  return function(students) {
    return rollCall('Math', students);
  };
}

let mathRollCall = makeMathRollCall();
mathRollCall(subjects['Math']);
// => Math:
// => Fatima
// => Gary
// => Susan
```

---

## 8. Advanced - later2 Function

**Question:** Write a function named `later2` that takes two arguments: a function and an argument for that function. The return value should be a new function that also takes an argument.

**Answer:**
```javascript
function later2(func, arg1) {
  return function(arg2) {
    return func(arg1, arg2);
  };
}

const notify = function(message, when) {
  console.log(`${message} in ${when} minutes!`);
};

let shutdownWarning = later2(notify, "The system is shutting down");
shutdownWarning(30); // The system is shutting down in 30 minutes!
```

---

## 9. Advanced (Conceptual) - bind for Partial Application

**Question:** Explain how `bind` can be used to create a function with pre-specified initial arguments, not just for setting context. Provide a code example.

**Answer:**
The `bind` method can accept additional arguments beyond the context object. These additional arguments are prepended to the arguments list when the bound function is called, effectively creating partial application.

```javascript
function multiply(a, b, c) {
  return a * b * c;
}

// Bind context (null) and first argument (2)
let double = multiply.bind(null, 2);

console.log(double(3, 4)); // 24 (2 * 3 * 4)

// Bind context and first two arguments
let multiplyBy2And3 = multiply.bind(null, 2, 3);
console.log(multiplyBy2And3(4)); // 24 (2 * 3 * 4)

// Practical example
function greet(greeting, punctuation, name) {
  console.log(greeting + ', ' + name + punctuation);
}

let sayHello = greet.bind(null, 'Hello', '!');
sayHello('Alice'); // Hello, Alice!
sayHello('Bob');   // Hello, Bob!
```

---

## 10. Advanced - Emulate bind's Context Binding

**Question:** Write a function that emulates the context-binding aspect of `bind`.

**Answer:**
```javascript
function bind(context, func) {
  return function() {
    return func.call(context);
  };
}

let obj = {};
let boundFunc = bind(obj, function() {
  this.foo = "bar";
});

boundFunc();
console.log(obj); // { foo: 'bar' }
```

**Enhanced version with arguments:**
```javascript
function bind(context, func) {
  return function(...args) {
    return func.apply(context, args);
  };
}

let obj = {};
let boundFunc = bind(obj, function(a, b) {
  this.sum = a + b;
});

boundFunc(5, 10);
console.log(obj); // { sum: 15 }
```

---

## 11. Intermediate (Conceptual) - Partial Application Definition

**Question:** Explain why the first `makeLogger` function is NOT an example of partial function application, but the second one is.

**Answer:**
```javascript
// Example 1 - NOT partial function application
function makeLogger(identifier) {
  return function(msg) {
    console.log(identifier + ' ' + msg); // Creates a single string argument
  };
}

// Example 2 - IS partial function application
function makeLogger(identifier) {
  return function(msg) {
    console.log(identifier, msg); // Passes two separate arguments
  };
}
```

**Explanation:**
Partial function application requires that the returned function calls the original function with fewer arguments than it normally expects. 

In Example 1, `console.log` is called with **one argument** (a concatenated string). The returned function doesn't reduce the number of arguments passed to `console.log`.

In Example 2, `console.log` is called with **two arguments** (`identifier` and `msg`). The `identifier` is pre-specified (partially applied) when `makeLogger` is called, and the returned function only needs to provide the remaining argument (`msg`). This is true partial application because we've reduced the number of arguments that need to be provided later.

---

## 12. Intermediate (Debugging) - bind Necessity

**Question:** What does the following code log to the console and why is `bind` necessary here?

```javascript
let person = {
  firstName: 'Peter',
  lastName: 'Parker',
  fullName() {
    console.log(this.firstName + ' ' + this.lastName +
                ' is the Amazing Spiderman!');
  },
};

let whoIsSpiderman = person.fullName.bind(person);
whoIsSpiderman();
```

**Answer:**
**Output:** `Peter Parker is the Amazing Spiderman!`

**Explanation:**
The `bind` is necessary because when we assign `person.fullName` to `whoIsSpiderman`, we lose the method's connection to the `person` object. Without `bind`, if we called `whoIsSpiderman()`, the execution context (`this`) would be the global object (or `undefined` in strict mode), not the `person` object.

```javascript
// Without bind - loses context
let whoIsSpiderman = person.fullName;
whoIsSpiderman(); // TypeError or undefined behavior

// With bind - preserves context
let whoIsSpiderman = person.fullName.bind(person);
whoIsSpiderman(); // Peter Parker is the Amazing Spiderman!
```

The `bind` method creates a new function that, when called, has its `this` keyword permanently set to `person`, ensuring the method can access `firstName` and `lastName` correctly.

---

# Additional Tricky Questions

## 13. Advanced - Multiple Partial Applications

**Question:** Create a `curry` function that allows you to partially apply arguments one at a time until all arguments are provided.

**Answer:**
```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func.apply(this, args);
    } else {
      return function(...moreArgs) {
        return curried.apply(this, args.concat(moreArgs));
      };
    }
  };
}

// Usage
function sum(a, b, c) {
  return a + b + c;
}

let curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3));     // 6
console.log(curriedSum(1, 2)(3));     // 6
console.log(curriedSum(1)(2, 3));     // 6
console.log(curriedSum(1, 2, 3));     // 6
```

---

## 14. Advanced - Partial from Right

**Question:** Implement a `partialRight` function that applies arguments from the right side instead of the left.

**Answer:**
```javascript
function partialRight(func, ...fixedArgs) {
  return function(...remainingArgs) {
    return func(...remainingArgs, ...fixedArgs);
  };
}

function divide(a, b) {
  return a / b;
}

let divideBy2 = partialRight(divide, 2);
console.log(divideBy2(10)); // 5 (10 / 2)

// Compare with regular partial application
function partial(func, ...fixedArgs) {
  return function(...remainingArgs) {
    return func(...fixedArgs, ...remainingArgs);
  };
}

let twoDiv = partial(divide, 2);
console.log(twoDiv(10)); // 0.2 (2 / 10)
```

---

## 15. Advanced - Debugging Closure Trap

**Question:** Explain what this code outputs and why. Then fix it using partial application.

```javascript
function createMultipliers() {
  let multipliers = [];
  
  for (var i = 1; i <= 3; i++) {
    multipliers.push(function(x) {
      return x * i;
    });
  }
  
  return multipliers;
}

let funcs = createMultipliers();
console.log(funcs[0](5)); // What does this output?
console.log(funcs[1](5));
console.log(funcs[2](5));
```

**Answer:**
**Current Output:**
```
20
20
20
```

All functions output `20` because they all share the same reference to `i`, which has the value `4` after the loop completes.

**Fixed with Partial Application:**
```javascript
function multiply(a, b) {
  return a * b;
}

function createMultipliers() {
  let multipliers = [];
  
  for (var i = 1; i <= 3; i++) {
    multipliers.push(
      (function(n) {
        return function(x) {
          return multiply(x, n);
        };
      })(i)
    );
  }
  
  return multipliers;
}

let funcs = createMultipliers();
console.log(funcs[0](5)); // 5
console.log(funcs[1](5)); // 10
console.log(funcs[2](5)); // 15
```

**Alternative Fix using let:**
```javascript
function createMultipliers() {
  let multipliers = [];
  
  for (let i = 1; i <= 3; i++) {  // Use 'let' instead of 'var'
    multipliers.push(function(x) {
      return x * i;
    });
  }
  
  return multipliers;
}
```

---

## 16. Advanced - Partial with Variable Arguments

**Question:** Create a `partial` function that can handle functions with any number of arguments and allows multiple rounds of partial application.

**Answer:**
```javascript
function partial(func, ...presetArgs) {
  return function(...laterArgs) {
    return func(...presetArgs, ...laterArgs);
  };
}

function greet(greeting, firstName, lastName, punctuation) {
  return `${greeting}, ${firstName} ${lastName}${punctuation}`;
}

let sayHello = partial(greet, 'Hello');
let sayHelloToJohn = partial(sayHello, 'John');
let sayHelloToJohnDoe = partial(sayHelloToJohn, 'Doe');

console.log(sayHelloToJohnDoe('!')); // Hello, John Doe!
console.log(sayHelloToJohn('Smith', '.')); // Hello, John Smith.
```

---

## 17. Tricky - Context Loss with Partial Application

**Question:** What's wrong with this code and how would you fix it?

```javascript
let calculator = {
  value: 0,
  add: function(n) {
    this.value += n;
    return this;
  },
  multiply: function(n) {
    this.value *= n;
    return this;
  }
};

function partial(func, arg) {
  return function() {
    return func(arg);
  };
}

let add5 = partial(calculator.add, 5);
add5(); // What happens here?
```

**Answer:**
The code will fail because `this` context is lost when we extract the method. 

**Fixed Version:**
```javascript
function partial(func, context, arg) {
  return function() {
    return func.call(context, arg);
  };
}

let add5 = partial(calculator.add, calculator, 5);
add5(); 
console.log(calculator.value); // 5

// Better approach using bind
let add5Better = calculator.add.bind(calculator, 5);
add5Better();
console.log(calculator.value); // 10
```

---

## 18. Advanced - Compose with Partial Application

**Question:** Create a `compose` function that combines function composition with partial application.

**Answer:**
```javascript
function compose(...funcs) {
  return function(x) {
    return funcs.reduceRight((acc, func) => func(acc), x);
  };
}

function multiply(a, b) {
  return a * b;
}

function add(a, b) {
  return a + b;
}

function square(x) {
  return x * x;
}

// Using bind for partial application
let multiplyBy2 = multiply.bind(null, 2);
let add3 = add.bind(null, 3);

let calculate = compose(square, add3, multiplyBy2);
console.log(calculate(5)); // ((5 * 2) + 3)^2 = 169
```

---

## 19. Tricky - Partial Application Order Matters

**Question:** Explain the difference in these two implementations and when you'd use each.

```javascript
// Version A
function partialA(func, ...args) {
  return function(...moreArgs) {
    return func(...args, ...moreArgs);
  };
}

// Version B
function partialB(func, ...args) {
  return function(...moreArgs) {
    return func(...moreArgs, ...args);
  };
}

function subtract(a, b) {
  return a - b;
}

let subFrom10A = partialA(subtract, 10);
let subFrom10B = partialB(subtract, 10);

console.log(subFrom10A(3)); // ?
console.log(subFrom10B(3)); // ?
```

**Answer:**
```javascript
console.log(subFrom10A(3)); // 7  (10 - 3)
console.log(subFrom10B(3)); // -7 (3 - 10)
```

**Version A** (left partial) prepends the fixed arguments - use when the fixed arguments should come first in the parameter list.

**Version B** (right partial) appends the fixed arguments - use when the fixed arguments should come last in the parameter list.

**Practical Example:**
```javascript
// Array.map expects: callback(element, index, array)
// If we want to create a partial with a divisor:

function divide(a, b) {
  return a / b;
}

// Right partial - better for Array.map
let halve = partialB(divide, 2);
console.log([10, 20, 30].map(halve)); // [5, 10, 15]

// Left partial - wouldn't work as expected
let wrongHalve = partialA(divide, 2);
console.log([10, 20, 30].map(wrongHalve)); // [0.2, 0.1, 0.066...]
```

---

## 20. Mind-Bender - Self-Referential Partial Application

**Question:** Create a recursive function that uses partial application to build a calculation chain.

**Answer:**
```javascript
function createChain(initialValue) {
  function chain(value) {
    chain.add = function(n) {
      return createChain(value + n);
    };
    
    chain.multiply = function(n) {
      return createChain(value * n);
    };
    
    chain.subtract = function(n) {
      return createChain(value - n);
    };
    
    chain.value = function() {
      return value;
    };
    
    return chain;
  }
  
  return chain(initialValue);
}

let result = createChain(5)
  .add(3)
  .multiply(2)
  .subtract(4)
  .value();

console.log(result); // 12
// Calculation: ((5 + 3) * 2) - 4 = 12
```
