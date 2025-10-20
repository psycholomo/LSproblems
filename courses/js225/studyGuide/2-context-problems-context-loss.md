# JavaScript Execution Context Practice Problems with Solutions

## Implicit Function Execution Context

### 1. **Difficulty: Basic**
**Question:** What does `this` point to in the code below?

```javascript
function whatIsMyContext() {
  return this;
}
```

**Answer:** In non-strict mode, `this` refers to the global object (`window` in browsers, `global` in Node.js). In strict mode, `this` would be `undefined`.

---

### 2. **Difficulty: Basic**
**Question:** What will the code below output?

```javascript
function foo() {
  return this;
}

let context = foo();
console.log(context);
```

**Answer:** In non-strict mode, this outputs the global object (`window` in browsers). In strict mode, it would output `undefined`.

---

### 3. **Difficulty: Basic**
**Question:** What will the code in the previous question output in strict mode?

**Answer:** `undefined` - In strict mode, when a function is called without an explicit context, `this` is `undefined` rather than the global object.

---

### 4. **Difficulty: Basic**
**Question:** What will the code below output? Explain the difference, if any, between this output and that of problem 2.

```javascript
let obj = {
  foo() {
    return this;
  },
};

let context = obj.foo();
console.log(context);
```

**Answer:** This outputs `obj` (the object itself). The difference is that when a function is invoked as a method (using `obj.foo()`), `this` is set to the calling object. In problem 2, the function was called standalone, so `this` defaulted to the global object.

---

### 5. **Difficulty: Intermediate**
**Question:** What does `this` point to in the code below?

```javascript
function foo() {
  function bar() {
    function baz() {
      console.log(this);
    }
    baz();
  }
  bar();
}

foo();
```

**Answer:** In non-strict mode, `this` points to the global object. In strict mode, it would be `undefined`. Nested regular functions don't inherit the context from their outer functions - each function call creates its own execution context.

---

### 6. **Difficulty: Intermediate**
**Question:** What will the code below output?

```javascript
var message = 'Hello from the global scope!';

function deliverMessage() {
  console.log(this.message);
}

deliverMessage();

let bar = {
  message: 'Hello from the function scope!',
};

bar.deliverMessage = deliverMessage;
bar.deliverMessage();
```

**Answer:**
- First call outputs: `"Hello from the global scope!"` (or `undefined` in strict mode)
- Second call outputs: `"Hello from the function scope!"`

The first call invokes the function standalone, so `this` refers to the global object. The second call invokes it as a method of `bar`, so `this` refers to `bar`.

---

### 7. **Difficulty: Advanced**
**Question:** What will the code below output? What would happen if we replaced `var` on line 1 with `let`? Can you explain why the output changes?

```javascript
var a = 10;
let b = 10;
let c = {
  a: -10,
  b: -10,
};

function add() {
  return this.a + b;
}

c.add = add;

console.log(add());
console.log(c.add());
```

**Answer:**
- `add()` outputs: `20` (in non-strict mode) or `NaN` (in strict mode, since `this` is `undefined`)
- `c.add()` outputs: `0`

First call: `this` is the global object, `this.a` is `10` (from `var a`), `b` is `10`, so `10 + 10 = 20`.
Second call: `this` is `c`, `this.a` is `-10`, `b` is `10`, so `-10 + 10 = 0`.

**If we replace `var` with `let`:** The first call would output `NaN` in non-strict mode (or throw an error in strict mode) because `let` doesn't create properties on the global object. So `this.a` would be `undefined`, and `undefined + 10 = NaN`.

---

## Explicit Function Execution Context

### 8. **Difficulty: Basic**
**Question:** What methods have we learned so far that let us explicitly specify what a function's execution context should be?

**Answer:** 
- `call()` - calls the function with a specified `this` value and arguments provided individually
- `apply()` - calls the function with a specified `this` value and arguments provided as an array
- `bind()` - returns a new function with a permanently bound `this` value

---

### 9. **Difficulty: Intermediate**
**Question:** In the code below, use `call` to invoke `bar.add` as a method but with `foo` as the execution context. What will this return?

```javascript
let foo = {
  a: 1,
  b: 2,
};

let bar = {
  a: 'abc',
  b: 'def',
  add() {
    return this.a + this.b;
  },
};
```

**Answer:**
```javascript
bar.add.call(foo); // Returns 3
```
This returns `3` because `this.a` is `1` and `this.b` is `2` from the `foo` object.

---

### 10. **Difficulty: Basic**
**Question:** What method can we use to permanently bind a function to a particular execution context?

**Answer:** `bind()` - It creates and returns a new function with a permanently bound execution context that cannot be changed, even with `call` or `apply`.

---

## Dealing with Context Loss and Hard Binding

### 11. **Difficulty: Intermediate**
**Question:** What will the code below log to console?

```javascript
let obj = {
  message: 'JavaScript',
};

function foo() {
  console.log(this.message);
}

foo.bind(obj);
```

**Answer:** Nothing! The `bind()` method returns a new function but doesn't invoke it. You need to call the returned function or save it to a variable and then call it.

---

### 12. **Difficulty: Intermediate**
**Question:** What will the code below output?

```javascript
let obj = {
  a: 2,
  b: 3,
};

function foo() {
  return this.a + this.b;
}

let bar = foo.bind(obj);
console.log(bar());
```

**Answer:** `5` - The `bind()` method creates a new function `bar` with `this` permanently bound to `obj`, so `this.a` is `2` and `this.b` is `3`.

---

### 13. **Difficulty: Advanced**
**Question:** What will the code below log to the console?

```javascript
let positiveMentality = {
  message: 'JavaScript makes sense!',
};

let negativeMentality = {
  message: 'JavaScript makes no sense!',
};

function foo() {
  console.log(this.message);
}

let bar = foo.bind(positiveMentality);

negativeMentality.logMessage = bar;
negativeMentality.logMessage();
```

**Answer:** `"JavaScript makes sense!"` - Once a function is bound using `bind()`, its `this` value is permanently set and cannot be changed, even when the function is called as a method of a different object.

---

### 14. **Difficulty: Advanced**
**Question:** What will the code below output?

```javascript
let obj = {
  a: 'Amazebulous!',
};
let otherObj = {
  a: "That's not a real word!",
};

function foo() {
  console.log(this.a);
}

let bar = foo.bind(obj);
bar.call(otherObj);
```

**Answer:** `"Amazebulous!"` - A bound function's context cannot be overridden, even with `call()` or `apply()`. The `bind()` method creates a permanent binding.

---

### 15. **Difficulty: Intermediate**
**Question:** In strict mode, what does the following program log to the console?

```javascript
function foo() {
  console.log(this.a);
}

let a = 2;
foo();
```

**Answer:** This throws a `TypeError: Cannot read property 'a' of undefined`. In strict mode, `this` is `undefined` when a function is called without an explicit context. Additionally, `let` declarations don't create properties on the global object, so even if `this` were the global object, `this.a` would still be `undefined`.

---

## Context Loss Problems

### 1. **Difficulty: Basic**
**Question:** What does the following code log to the console? Explain why.

```javascript
let turk = {
  firstName: 'Christopher',
  lastName: 'Turk',
  getDescription() {
    return 'My name is ' + this.firstName + ' ' + this.lastName + '.';
  },
};

let getTurkDescription = turk.getDescription;
console.log(getTurkDescription());
```

**Answer:** `"My name is undefined undefined."` (in non-strict mode) or throws a `TypeError` (in strict mode).

When we assign `turk.getDescription` to `getTurkDescription`, we're extracting the method from the object. When we call `getTurkDescription()`, it's called as a standalone function, not as a method, so `this` is the global object (or `undefined` in strict mode), which doesn't have `firstName` or `lastName` properties.

---

### 2. **Difficulty: Intermediate**
**Question:** The code from the previous problem fails to produce the desired output. How can you fix it by altering only the last line of code?

**Answer:** Use `call()` or `apply()`:
```javascript
console.log(getTurkDescription.call(turk));
// or
console.log(getTurkDescription.apply(turk));
// or simply
console.log(turk.getDescription());
```

---

### 3. **Difficulty: Intermediate**
**Question:** Let's say we want to create a new function called `logDescription` that we can call without worrying about context. Create `logDescription` by permanently binding `turk.getDescription` to the `turk` object.

**Answer:**
```javascript
let logDescription = turk.getDescription.bind(turk);
console.log(logDescription()); // Works correctly
```

---

### 4. **Difficulty: Intermediate**
**Question:** Consider the following code. Will this code produce the desired output? Why or why not?

```javascript
// Desired output:
// The Elder Scrolls: Arena
// The Elder Scrolls: Daggerfall
// The Elder Scrolls: Morrowind
// The Elder Scrolls: Oblivion
// The Elder Scrolls: Skyrim

const TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames: function() {
    this.titles.forEach(function(title) {
      console.log(this.seriesTitle + ': ' + title);
    });
  }
};

TESgames.listGames();
```

**Answer:** No, it will output `"undefined: Arena"`, `"undefined: Daggerfall"`, etc. (or throw an error in strict mode).

The callback function passed to `forEach` loses context. Inside the callback, `this` refers to the global object (or `undefined` in strict mode), not `TESgames`, so `this.seriesTitle` is `undefined`.

---

### 5. **Difficulty: Intermediate**
**Question:** Fix the code from the previous problem by using the `let self = this;` pattern to preserve the context within the forEach callback.

**Answer:**
```javascript
const TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames: function() {
    let self = this;
    this.titles.forEach(function(title) {
      console.log(self.seriesTitle + ': ' + title);
    });
  }
};

TESgames.listGames();
```

---

### 6. **Difficulty: Intermediate**
**Question:** The `forEach` method provides another way to supply the execution context for its callback function. Modify the program from problem 4 to use this technique to produce the proper output.

**Answer:**
```javascript
const TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames: function() {
    this.titles.forEach(function(title) {
      console.log(this.seriesTitle + ': ' + title);
    }, this); // Pass 'this' as the second argument to forEach
  }
};

TESgames.listGames();
```

---

### 7. **Difficulty: Intermediate**
**Question:** Another way to solve the issue in problem 4 is to use `bind`. Modify the code to use `bind` on the callback function to ensure `this` refers to `TESgames`.

**Answer:**
```javascript
const TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames: function() {
    this.titles.forEach(function(title) {
      console.log(this.seriesTitle + ': ' + title);
    }.bind(this));
  }
};

TESgames.listGames();
```

---

### 8. **Difficulty: Intermediate**
**Question:** Modern JavaScript offers a concise way to handle context loss with callbacks. Refactor the code from problem 4 to use an arrow function for the callback.

**Answer:**
```javascript
const TESgames = {
  titles: ['Arena', 'Daggerfall', 'Morrowind', 'Oblivion', 'Skyrim'],
  seriesTitle: 'The Elder Scrolls',
  listGames: function() {
    this.titles.forEach(title => {
      console.log(this.seriesTitle + ': ' + title);
    });
  }
};

TESgames.listGames();
```

Arrow functions don't have their own `this` binding; they inherit `this` from the enclosing scope.

---

### 9. **Difficulty: Advanced**
**Question:** What will the following code log to the console? Explain your answer.

```javascript
let computer = {
  brand: 'Apple',
  year: '2023',
  getInfo() {
    console.log(`This is a ${this.year} ${this.brand} computer.`);
  }
};

let otherComputer = {
  brand: 'Dell',
  year: '2021',
};

let getComputerInfo = computer.getInfo.bind(computer);
getComputerInfo.call(otherComputer);
```

**Answer:** `"This is a 2023 Apple computer."`

Even though we try to use `call()` to change the context to `otherComputer`, the function was already permanently bound to `computer` using `bind()`. Once bound, a function's context cannot be changed by `call()`, `apply()`, or any other method.

---

### 10. **Difficulty: Advanced**
**Question:** The `incrementA` method in the code below is not working as intended. It should increment `foo.a` by 1. What is the problem, and how would you fix it?

```javascript
let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }
    increment();
  }
};

foo.incrementA();
console.log(foo.a); // Expected output: 1
```

**Answer:** The problem is that the `increment` function loses context. When called as a standalone function, `this` inside `increment` refers to the global object (or is `undefined` in strict mode), not `foo`.

**Solutions:**

**Option 1: Use an arrow function**
```javascript
let foo = {
  a: 0,
  incrementA() {
    const increment = () => {
      this.a += 1;
    };
    increment();
  }
};
```

**Option 2: Use `bind()`**
```javascript
let foo = {
  a: 0,
  incrementA() {
    function increment() {
      this.a += 1;
    }
    increment.call(this);
    // or increment.bind(this)();
  }
};
```

**Option 3: Preserve context with a variable**
```javascript
let foo = {
  a: 0,
  incrementA() {
    let self = this;
    function increment() {
      self.a += 1;
    }
    increment();
  }
};
```

---

## Additional Tricky/Difficult Problems

### 11. **Difficulty: Advanced**
**Question:** What will the following code output? Explain the surprising behavior.

```javascript
const obj = {
  name: 'Object',
  arrowFunc: () => {
    console.log(this.name);
  },
  regularFunc() {
    console.log(this.name);
  }
};

obj.arrowFunc();
obj.regularFunc();
```

**Answer:**
- `obj.arrowFunc()` outputs: `undefined` (or the global `name` if it exists)
- `obj.regularFunc()` outputs: `"Object"`

**Explanation:** Arrow functions don't have their own `this` binding. They inherit `this` from the enclosing lexical scope at the time they're defined. Since `arrowFunc` is defined in the global scope (object literals don't create a new scope), `this` refers to the global object, not `obj`. Regular functions, however, get their `this` set based on how they're called.

---

### 12. **Difficulty: Advanced**
**Question:** Predict the output and explain what happens:

```javascript
function Person(name) {
  this.name = name;
  this.greet = function() {
    console.log(`Hello, I'm ${this.name}`);
  };
  
  setTimeout(this.greet, 1000);
}

const person = new Person('Alice');
```

**Answer:** After 1 second, it outputs `"Hello, I'm undefined"` (or throws an error in strict mode).

**Explanation:** When `this.greet` is passed to `setTimeout`, it loses its connection to the `person` object. `setTimeout` calls the function in the global context, so `this` inside `greet` refers to the global object (or `undefined` in strict mode).

**Fix:**
```javascript
setTimeout(this.greet.bind(this), 1000);
// or
setTimeout(() => this.greet(), 1000);
```

---

### 13. **Difficulty: Expert**
**Question:** What will this code output? This is a particularly tricky one!

```javascript
var length = 5;

function callback() {
  console.log(this.length);
}

const obj = {
  length: 10,
  method(fn) {
    fn();
    arguments[0]();
  }
};

obj.method(callback, 1, 2, 3);
```

**Answer:**
- First `console.log` outputs: `5` (the global `length`)
- Second `console.log` outputs: `4`

**Explanation:**
- `fn()` is called as a standalone function, so `this` is the global object, and `this.length` is `5`.
- `arguments[0]()` is calling the function as a method of the `arguments` object! The `arguments` object has a `length` property equal to the number of arguments passed (4 in this case: `callback, 1, 2, 3`), so `this.length` is `4`.

---

### 14. **Difficulty: Expert**
**Question:** What will this code log? Explain the chain of context changes.

```javascript
const calculator = {
  value: 0,
  add: function(n) {
    this.value += n;
    return this;
  },
  subtract: function(n) {
    this.value -= n;
    return this;
  },
  getValue: () => {
    return this.value;
  }
};

const result = calculator.add(10).subtract(3).getValue();
console.log(result);
```

**Answer:** `undefined` (or whatever `this.value` is in the global scope)

**Explanation:** The `add` and `subtract` methods work correctly because they're regular functions and return `this` (the `calculator` object), enabling method chaining. However, `getValue` is an arrow function, which doesn't have its own `this` binding. It inherits `this` from the enclosing lexical scope (global scope), so `this.value` refers to the global `value`, not `calculator.value`.

**Fix:** Change `getValue` to a regular function:
```javascript
getValue: function() {
  return this.value;
}
// or
getValue() {
  return this.value;
}
```

---

### 15. **Difficulty: Expert**
**Question:** What happens in this code? Why doesn't the double bind work as expected?

```javascript
function greet() {
  console.log(`Hello, ${this.name}!`);
}

const person1 = { name: 'Alice' };
const person2 = { name: 'Bob' };

const greetAlice = greet.bind(person1);
const greetBob = greetAlice.bind(person2);

greetBob();
```

**Answer:** Outputs `"Hello, Alice!"`

**Explanation:** You cannot rebind a function that has already been bound. The first `bind(person1)` permanently sets the context to `person1`. The second `bind(person2)` creates a new function, but it cannot override the context that was already bound. Once a function is bound, its `this` value is locked and cannot be changed.

---

### 16. **Difficulty: Expert**
**Question:** Identify all the context loss issues in this code and fix them:

```javascript
const library = {
  books: ['1984', 'Brave New World', 'Fahrenheit 451'],
  name: 'City Library',
  
  displayBooks: function() {
    console.log(`Books in ${this.name}:`);
    
    this.books.forEach(function(book) {
      setTimeout(function() {
        console.log(`- ${book} from ${this.name}`);
      }, 100);
    });
  }
};

library.displayBooks();
```

**Answer:** There are TWO context losses:
1. The `forEach` callback loses context (though it doesn't use `this`, so it's not a problem here)
2. The `setTimeout` callback loses context

**Fixed version:**
```javascript
const library = {
  books: ['1984', 'Brave New World', 'Fahrenheit 451'],
  name: 'City Library',
  
  displayBooks: function() {
    console.log(`Books in ${this.name}:`);
    
    this.books.forEach(book => {
      setTimeout(() => {
        console.log(`- ${book} from ${this.name}`);
      }, 100);
    });
  }
};

library.displayBooks();
```

Or using `bind`:
```javascript
this.books.forEach(function(book) {
  setTimeout(function() {
    console.log(`- ${book} from ${this.name}`);
  }.bind(this), 100);
}.bind(this));
```

---

These problems progressively build understanding of JavaScript's execution context, from basic concepts to very tricky edge cases!