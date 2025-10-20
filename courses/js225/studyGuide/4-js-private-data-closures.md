# JavaScript Closures and Private Data - Complete Guide

## Conceptual Questions

### 1. **Difficulty: Basic**
**Question:** What is "private data" in the context of JavaScript, and why is it considered a beneficial feature in object-oriented programming?

<details>
<summary><strong>Answer</strong></summary>

Private data refers to variables or properties that cannot be accessed or modified directly from outside their enclosing scope. In JavaScript, this is achieved through closures and function scopes.

**Benefits:**
- **Encapsulation**: Hides implementation details
- **Data integrity**: Prevents accidental or malicious modification
- **Interface control**: Only exposes necessary methods/properties
- **Reduces bugs**: Limits where data can be changed
- **Modularity**: Creates cleaner, more maintainable code

</details>

---

### 2. **Difficulty: Basic**
**Question:** Explain how closures enable the creation of private data and state in JavaScript. Provide a simple code example to illustrate your explanation.

<details>
<summary><strong>Answer</strong></summary>

Closures enable private data by creating a scope that persists even after the outer function has executed. Inner functions maintain access to the outer function's variables, but those variables remain inaccessible from outside.

**Example:**
```javascript
function createPerson(name) {
  // 'name' is private - only accessible within this scope
  let age = 0;
  
  return {
    getName: function() {
      return name;
    },
    getAge: function() {
      return age;
    },
    haveBirthday: function() {
      age++;
    }
  };
}

let person = createPerson('Alice');
console.log(person.getName()); // 'Alice'
person.haveBirthday();
console.log(person.getAge()); // 1
// console.log(person.name); // undefined - private!
```

</details>

---

### 3. **Difficulty: Intermediate**
**Question:** What is an IIFE (Immediately Invoked Function Expression)? Describe how an IIFE can be used to create a module or object that has private functions and variables.

<details>
<summary><strong>Answer</strong></summary>

An IIFE (Immediately Invoked Function Expression) is a function that is defined and executed immediately. It's written as `(function() { ... })()`.

**Module Pattern Example:**
```javascript
let calculator = (function() {
  // Private variables and functions
  let result = 0;
  
  function log(operation) {
    console.log(`Operation: ${operation}, Result: ${result}`);
  }
  
  // Public API
  return {
    add: function(x) {
      result += x;
      log('add');
      return this;
    },
    subtract: function(x) {
      result -= x;
      log('subtract');
      return this;
    },
    getResult: function() {
      return result;
    }
  };
})();

calculator.add(5).subtract(2);
console.log(calculator.getResult()); // 3
// calculator.result is undefined (private)
// calculator.log is undefined (private)
```

</details>

---

### 4. **Difficulty: Intermediate**
**Question:** Even when data is "private" within a closure, it's possible to unintentionally expose it or allow it to be mutated from outside code. Describe one common way this can happen and suggest a strategy to prevent it.

<details>
<summary><strong>Answer</strong></summary>

**Common way to expose private data:**
Returning a reference to a mutable object (arrays, objects) allows external code to modify it.

```javascript
// PROBLEMATIC:
function makeData() {
  let items = ['a', 'b', 'c'];
  return {
    getItems: function() {
      return items; // Returns reference!
    }
  };
}

let data = makeData();
let myItems = data.getItems();
myItems.push('d'); // Mutates private data!
```

**Prevention strategies:**
1. Return a copy: `return [...items]` or `return items.slice()`
2. Return a frozen copy: `return Object.freeze([...items])`
3. Use defensive copying for objects: `return {...obj}` or `JSON.parse(JSON.stringify(obj))`

</details>

---

### 5. **Difficulty: Advanced**
**Question:** Given the following code, is there any way to access or modify the `status` variable from the global scope without changing the `startup` function itself? Explain why or why not.

```javascript
function startup() {
  let status = 'ready';
  return function() {
    console.log('The system is ready.');
  };
}

let ready = startup();
```

<details>
<summary><strong>Answer</strong></summary>

**No**, there is no way to access or modify the `status` variable from the global scope without changing the `startup` function itself.

**Explanation:**
- The `status` variable is locally scoped to the `startup` function
- The returned function doesn't reference `status` in any way (no closure over it)
- Once `startup()` completes, `status` becomes eligible for garbage collection
- JavaScript doesn't provide reflection mechanisms to access variables in closed-over scopes that aren't referenced by any living closures
- Even developer tools can't access it because there's no closure maintaining the reference

If the returned function used `status`, it would create a closure and the variable would persist, but it still wouldn't be accessible from outside.

</details>

---

### 6. **Difficulty: Intermediate** *(NEW)*
**Question:** Explain the difference between using closures for private data versus using JavaScript's new `#` private field syntax in classes. What are the advantages and disadvantages of each approach?

<details>
<summary><strong>Answer</strong></summary>

**Closures for Private Data:**
```javascript
function Person(name) {
  let _name = name; // private via closure
  
  this.getName = function() {
    return _name;
  };
}
```

**Advantages:**
- Works in all JavaScript environments
- More flexible (can create private data in any function)
- Can be used with factory functions (no `new` keyword needed)

**Disadvantages:**
- Methods are recreated for each instance (memory overhead)
- Slightly harder to understand for beginners

**Class Private Fields (`#`):**
```javascript
class Person {
  #name; // truly private field
  
  constructor(name) {
    this.#name = name;
  }
  
  getName() {
    return this.#name;
  }
}
```

**Advantages:**
- Methods shared via prototype (better memory efficiency)
- Clearer syntax
- Truly private (syntactic enforcement)
- Better performance

**Disadvantages:**
- Only works in classes
- Requires modern JavaScript support
- Can't be used with object literals

</details>

---

### 7. **Difficulty: Advanced** *(NEW)*
**Question:** What is a "memory leak" in the context of closures? Describe a scenario where improper use of closures could lead to memory issues and how you would prevent it.

<details>
<summary><strong>Answer</strong></summary>

A memory leak with closures occurs when unintended references prevent garbage collection.

**Scenario:**
```javascript
// PROBLEMATIC:
function attachHandlers() {
  let largeData = new Array(1000000).fill('data');
  
  document.getElementById('button').addEventListener('click', function() {
    console.log('Clicked');
    // This closure captures largeData even though it doesn't use it!
  });
}

// Each time attachHandlers() is called, a new closure is created
// that keeps largeData in memory, even if we never use it
```

**Problems:**
- The event handler closure captures the entire scope, including `largeData`
- If `attachHandlers()` is called multiple times, memory accumulates
- Old event handlers aren't removed, causing leaks

**Prevention:**
```javascript
// SOLUTION 1: Only capture what you need
function attachHandlers() {
  let largeData = new Array(1000000).fill('data');
  let summary = largeData.length; // Extract only needed data
  
  document.getElementById('button').addEventListener('click', function() {
    console.log('Clicked, data size:', summary);
    // Only 'summary' is captured, not largeData
  });
}

// SOLUTION 2: Remove event listeners when done
function attachHandlers() {
  let largeData = new Array(1000000).fill('data');
  
  function handler() {
    console.log('Clicked');
  }
  
  let button = document.getElementById('button');
  button.addEventListener('click', handler);
  
  // Later: clean up
  return function cleanup() {
    button.removeEventListener('click', handler);
  };
}

// SOLUTION 3: Set references to null when done
function attachHandlers() {
  let largeData = new Array(1000000).fill('data');
  
  // Use data...
  processData(largeData);
  
  largeData = null; // Allow garbage collection
  
  document.getElementById('button').addEventListener('click', function() {
    console.log('Clicked');
  });
}
```

</details>

---

## Coding Exercises

### 8. **Difficulty: Basic**
**Problem:** Create a function `makeCounter` that returns a new function. The returned function, when invoked, should increment a private counter and log the new value. Each counter created should be independent.

```javascript
let counter1 = makeCounter();
counter1(); // logs 1
counter1(); // logs 2

let counter2 = makeCounter();
counter2(); // logs 1
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeCounter() {
  let count = 0;
  
  return function() {
    count++;
    console.log(count);
  };
}

let counter1 = makeCounter();
counter1(); // logs 1
counter1(); // logs 2

let counter2 = makeCounter();
counter2(); // logs 1
```

</details>

---

### 9. **Difficulty: Intermediate**
**Problem:** Write a function named `makeMultipleLister` that takes a number as an argument. It should return a function that, when invoked, logs every positive integer multiple of the base number that is less than 100. The returned function should not take any arguments.

```javascript
let lister = makeMultipleLister(13);
lister();
// 13
// 26
// 39
// 52
// 65
// 78
// 91
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeMultipleLister(base) {
  return function() {
    for (let multiple = base; multiple < 100; multiple += base) {
      console.log(multiple);
    }
  };
}

let lister = makeMultipleLister(13);
lister();
// 13
// 26
// 39
// 52
// 65
// 78
// 91
```

</details>

---

### 10. **Difficulty: Intermediate**
**Problem:** Using an IIFE, create a `generateStudentId` function that is solely responsible for keeping track of a student ID counter. The counter should not be exposed to the global scope. Each time the function is called, it should return a new, unique student ID, starting from 1.

```javascript
console.log(generateStudentId()); // 1
console.log(generateStudentId()); // 2
console.log(generateStudentId()); // 3
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
let generateStudentId = (function() {
  let currentId = 0;
  
  return function() {
    currentId++;
    return currentId;
  };
})();

console.log(generateStudentId()); // 1
console.log(generateStudentId()); // 2
console.log(generateStudentId()); // 3
```

</details>

---

### 11. **Difficulty: Intermediate**
**Problem:** Write a `makeList` function that creates and returns a new function that implements a todo list. The list of items must be private.

The returned function should exhibit the following behavior:
- When called with a string argument that is not already on the list, it adds the string to the list and logs a confirmation message (e.g., "item added!").
- When called with a string argument that is already on the list, it removes the item from the list and logs a confirmation message (e.g., "item removed!").
- When called with no arguments, it logs all items on the list. If the list is empty, it logs an appropriate message.

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeList() {
  let items = [];
  
  return function(item) {
    if (item === undefined) {
      if (items.length === 0) {
        console.log('The list is empty.');
      } else {
        items.forEach(function(item) {
          console.log(item);
        });
      }
    } else {
      let index = items.indexOf(item);
      if (index === -1) {
        items.push(item);
        console.log(item + ' added!');
      } else {
        items.splice(index, 1);
        console.log(item + ' removed!');
      }
    }
  };
}

let list = makeList();
list('buy milk');      // buy milk added!
list('buy eggs');      // buy eggs added!
list();                // buy milk
                       // buy eggs
list('buy milk');      // buy milk removed!
list();                // buy eggs
```

</details>

---

### 12. **Difficulty: Intermediate**
**Problem:** Refactor the `makeList` function from the previous problem. Instead of returning a single function, it should return an object with three methods: `add(item)`, `remove(item)`, and `list()`. The underlying array of items must remain private to the object.

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeList() {
  let items = [];
  
  return {
    add: function(item) {
      let index = items.indexOf(item);
      if (index === -1) {
        items.push(item);
        console.log(item + ' added!');
      } else {
        console.log(item + ' is already on the list.');
      }
    },
    
    remove: function(item) {
      let index = items.indexOf(item);
      if (index !== -1) {
        items.splice(index, 1);
        console.log(item + ' removed!');
      } else {
        console.log(item + ' is not on the list.');
      }
    },
    
    list: function() {
      if (items.length === 0) {
        console.log('The list is empty.');
      } else {
        items.forEach(function(item) {
          console.log(item);
        });
      }
    }
  };
}

let list = makeList();
list.add('buy milk');
list.add('buy eggs');
list.list();
list.remove('buy milk');
list.list();
```

</details>

---

### 13. **Difficulty: Advanced**
**Problem:** Create a factory function `makeBankAccount` that returns a bank account object. The object should have the methods `deposit(amount)`, `withdraw(amount)`, and `balance()`. The actual balance value must be private.

- `deposit(amount)` should add to the balance.
- `withdraw(amount)` should subtract from the balance but should not allow the balance to go below zero. If the withdrawal amount is too high, it should log an error and not change the balance.
- `balance()` should return the current balance.

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeBankAccount() {
  let balance = 0;
  
  return {
    deposit: function(amount) {
      if (amount > 0) {
        balance += amount;
        console.log(`Deposited: $${amount}. New balance: $${balance}`);
      } else {
        console.log('Deposit amount must be positive.');
      }
      return this;
    },
    
    withdraw: function(amount) {
      if (amount > balance) {
        console.log('Insufficient funds. Withdrawal cancelled.');
      } else if (amount <= 0) {
        console.log('Withdrawal amount must be positive.');
      } else {
        balance -= amount;
        console.log(`Withdrew: $${amount}. New balance: $${balance}`);
      }
      return this;
    },
    
    balance: function() {
      return balance;
    }
  };
}

let account = makeBankAccount();
account.deposit(100);       // Deposited: $100. New balance: $100
account.withdraw(50);       // Withdrew: $50. New balance: $50
console.log(account.balance()); // 50
account.withdraw(100);      // Insufficient funds. Withdrawal cancelled.
```

</details>

---

### 14. **Difficulty: Advanced**
**Problem:** Create a `passwordManager` object using an IIFE. It must have methods `add(service, password)` and `getPassword(service)`. It should store credentials in a private object. The internal credential store must not be accessible from the outside.

<details>
<summary><strong>Solution</strong></summary>

```javascript
let passwordManager = (function() {
  let credentials = {};
  
  return {
    add: function(service, password) {
      credentials[service] = password;
      console.log(`Password for ${service} has been saved.`);
    },
    
    getPassword: function(service) {
      if (credentials[service]) {
        return credentials[service];
      } else {
        console.log(`No password found for ${service}.`);
        return undefined;
      }
    }
  };
})();

passwordManager.add('gmail', 'myP@ssw0rd');
console.log(passwordManager.getPassword('gmail')); // myP@ssw0rd
console.log(passwordManager.getPassword('facebook')); // No password found...
// passwordManager.credentials is undefined (private)
```

</details>

---

### 15. **Difficulty: Basic** *(NEW)*
**Problem:** Create a function `makeGreeter` that takes a name as an argument and returns a function. The returned function should greet the person by name when called. The name should be stored privately.

```javascript
let greetAlice = makeGreeter('Alice');
greetAlice(); // logs "Hello, Alice!"

let greetBob = makeGreeter('Bob');
greetBob(); // logs "Hello, Bob!"
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeGreeter(name) {
  return function() {
    console.log(`Hello, ${name}!`);
  };
}

let greetAlice = makeGreeter('Alice');
greetAlice(); // logs "Hello, Alice!"

let greetBob = makeGreeter('Bob');
greetBob(); // logs "Hello, Bob!"
```

</details>

---

### 16. **Difficulty: Intermediate** *(NEW)*
**Problem:** Create a `makeTimer` function that returns an object with methods `start()`, `stop()`, and `getElapsed()`. The timer should track elapsed time in seconds privately. 

- `start()` begins the timer (or does nothing if already running)
- `stop()` stops the timer
- `getElapsed()` returns the total elapsed time in seconds

```javascript
let timer = makeTimer();
timer.start();
// ... some time passes ...
timer.stop();
console.log(timer.getElapsed()); // logs elapsed time in seconds
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeTimer() {
  let startTime = null;
  let elapsed = 0;
  let running = false;
  
  return {
    start: function() {
      if (!running) {
        startTime = Date.now();
        running = true;
      }
    },
    
    stop: function() {
      if (running) {
        elapsed += (Date.now() - startTime) / 1000;
        running = false;
      }
    },
    
    getElapsed: function() {
      if (running) {
        return elapsed + (Date.now() - startTime) / 1000;
      }
      return elapsed;
    },
    
    reset: function() {
      startTime = null;
      elapsed = 0;
      running = false;
    }
  };
}

let timer = makeTimer();
timer.start();
setTimeout(() => {
  timer.stop();
  console.log(timer.getElapsed()); // approximately 2
}, 2000);
```

</details>

---

### 17. **Difficulty: Intermediate** *(NEW)*
**Problem:** Write a function `makeStack` that creates a stack data structure with private data. It should return an object with methods `push(item)`, `pop()`, and `peek()`.

- `push(item)` adds an item to the top of the stack
- `pop()` removes and returns the top item (returns `undefined` if empty)
- `peek()` returns the top item without removing it (returns `undefined` if empty)

```javascript
let stack = makeStack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.peek()); // 3
console.log(stack.pop());  // 3
console.log(stack.peek()); // 2
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeStack() {
  let items = [];
  
  return {
    push: function(item) {
      items.push(item);
    },
    
    pop: function() {
      return items.pop();
    },
    
    peek: function() {
      return items[items.length - 1];
    },
    
    size: function() {
      return items.length;
    },
    
    isEmpty: function() {
      return items.length === 0;
    }
  };
}

let stack = makeStack();
stack.push(1);
stack.push(2);
stack.push(3);
console.log(stack.peek()); // 3
console.log(stack.pop());  // 3
console.log(stack.peek()); // 2
```

</details>

---

### 18. **Difficulty: Advanced** *(NEW)*
**Problem:** Create a `rateLimiter` function using closures. It should take a function and a time limit (in milliseconds) as arguments. It returns a new function that can only be called once within the specified time limit. Subsequent calls within that time should be ignored.

```javascript
function logMessage(msg) {
  console.log(msg);
}

let limitedLog = rateLimiter(logMessage, 2000);
limitedLog('First call');  // logs "First call"
limitedLog('Second call'); // ignored (within 2 seconds)
// After 2 seconds:
limitedLog('Third call');  // logs "Third call"
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function rateLimiter(fn, timeLimit) {
  let lastCallTime = 0;
  
  return function(...args) {
    let now = Date.now();
    
    if (now - lastCallTime >= timeLimit) {
      lastCallTime = now;
      return fn.apply(this, args);
    }
    // Call is ignored if within time limit
  };
}

function logMessage(msg) {
  console.log(msg);
}

let limitedLog = rateLimiter(logMessage, 2000);
limitedLog('First call');  // logs "First call"
limitedLog('Second call'); // ignored
setTimeout(() => {
  limitedLog('Third call'); // logs "Third call"
}, 2100);
```

</details>

---

### 19. **Difficulty: Advanced** *(NEW)*
**Problem:** Create a `makeCache` function that implements a simple memoization cache with a maximum size limit. When the cache is full and a new item is added, the oldest item should be removed. The cache should be completely private.

The returned object should have methods:
- `set(key, value)` - adds or updates a value
- `get(key)` - retrieves a value (returns `undefined` if not found)
- `has(key)` - checks if a key exists
- `size()` - returns the current number of items

```javascript
let cache = makeCache(3); // max 3 items
cache.set('a', 1);
cache.set('b', 2);
cache.set('c', 3);
cache.set('d', 4); // 'a' should be removed
console.log(cache.has('a')); // false
console.log(cache.get('b')); // 2
console.log(cache.size());   // 3
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeCache(maxSize) {
  let cache = new Map();
  let keys = []; // Track insertion order
  
  return {
    set: function(key, value) {
      if (cache.has(key)) {
        cache.set(key, value);
      } else {
        if (cache.size >= maxSize) {
          // Remove oldest (first) item
          let oldestKey = keys.shift();
          cache.delete(oldestKey);
        }
        cache.set(key, value);
        keys.push(key);
      }
    },
    
    get: function(key) {
      return cache.get(key);
    },
    
    has: function(key) {
      return cache.has(key);
    },
    
    size: function() {
      return cache.size;
    },
    
    clear: function() {
      cache.clear();
      keys = [];
    }
  };
}

let cache = makeCache(3);
cache.set('a', 1);
cache.set('b', 2);
cache.set('c', 3);
cache.set('d', 4); // 'a' is removed
console.log(cache.has('a')); // false
console.log(cache.get('b')); // 2
console.log(cache.size());   // 3
```

</details>

---

## Debugging Exercises

### 20. **Difficulty: Intermediate**
**Problem:** The following code attempts to create a person object with a private name. However, the name can still be changed from outside. Identify the bug and explain how to fix it so the name is truly private and can only be set once.

```javascript
function makePerson(name) {
  return {
    name: name,
    rename: function(newName) {
      this.name = newName;
    },
    getName: function() {
      return this.name;
    }
  };
}

let person = makePerson('Alice');
console.log(person.getName()); // 'Alice'
person.name = 'Bob'; // This should not be possible
console.log(person.getName()); // 'Bob'
```

<details>
<summary><strong>Solution</strong></summary>

**Problem:** The `name` property is directly accessible on the returned object.

**Fixed Code:**
```javascript
function makePerson(name) {
  // Don't expose name as a property
  // Keep it as a local variable
  
  return {
    getName: function() {
      return name;
    }
    // Remove rename method if name should be immutable
    // Or keep it to allow internal updates only
  };
}

let person = makePerson('Alice');
console.log(person.getName()); // 'Alice'
person.name = 'Bob'; // This creates a new property, doesn't affect private name
console.log(person.getName()); // 'Alice' (unchanged)
```

**Explanation:** By keeping `name` as a local variable instead of an object property, it becomes truly private and accessible only through the closure.

</details>

---

### 21. **Difficulty: Advanced**
**Problem:** The `makeList` function below is intended to keep its items array private. However, the private data can be mutated by external code. Identify the flaw in the `list` method and correct it.

```javascript
function makeList() {
  let items = [];

  return {
    add: function(item) {
      items.push(item);
    },
    list: function() {
      // This line has a flaw
      return items;
    },
  };
}

let list = makeList();
list.add('peas');
let groceries = list.list(); // Get a reference to the private array
groceries.push('corn');      // Mutate the private array

// list() should only return ['peas'], but it returns ['peas', 'corn']
console.log(list.list());
```

<details>
<summary><strong>Solution</strong></summary>

**Problem:** The `list()` method returns a reference to the private array, allowing external mutation.

**Fixed Code:**
```javascript
function makeList() {
  let items = [];

  return {
    add: function(item) {
      items.push(item);
    },
    list: function() {
      // Return a copy instead of the original reference
      return items.slice(); // or [...items]
    },
  };
}

let list = makeList();
list.add('peas');
let groceries = list.list();
groceries.push('corn'); // Only affects the copy

console.log(list.list()); // ['peas'] - private array unaffected
```

**Explanation:** Always return copies of mutable objects to prevent external code from modifying private data.

</details>

---

### 22. **Difficulty: Advanced**
**Problem:** The `ItemManager` is supposed to manage a private collection of items. The `create` method has a bug that prevents it from working as intended. Find and fix the bug.

```javascript
let ItemManager = (function() {
  let items = [];

  return {
    create: function(itemName, category, quantity) {
      let item = {
        itemName: itemName,
        category: category,
        quantity: quantity,
      };
      // `this` does not refer to the expected object here.
      this.items.push(item);
    },

    list: function() {
      console.log(items);
    },
  };
})();

ItemManager.create('Lasagna', 'Pasta', 5);
ItemManager.list(); // Expected to log the lasagna item, but an error occurs.
```

<details>
<summary><strong>Solution</strong></summary>

**Problem:** Using `this.items` instead of the private `items` variable.

**Fixed Code:**
```javascript
let ItemManager = (function() {
  let items = [];

  return {
    create: function(itemName, category, quantity) {
      let item = {
        itemName: itemName,
        category: category,
        quantity: quantity,
      };
      // Use the private variable 'items', not 'this.items'
      items.push(item);
    },

    list: function() {
      console.log(items);
    },
  };
})();

ItemManager.create('Lasagna', 'Pasta', 5);
ItemManager.list(); // [{ itemName: 'Lasagna', category: 'Pasta', quantity: 5 }]
```

**Explanation:** The `items` array is a private variable in the IIFE's closure, not a property of the returned object. Use `items` directly, not `this.items`.

</details>

---

### 23. **Difficulty: Intermediate** *(NEW)*
**Problem:** The following code attempts to create multiple independent counters, but they all share the same count. Identify and fix the bug.

```javascript
function makeCounters(n) {
  let counters = [];
  for (var i = 0; i < n; i++) {
    counters.push(function() {
      console.log(i);
    });
  }
  return counters;
}

let myCounters = makeCounters(3);
myCounters[0](); // Expected: 0, Actual: ?
myCounters[1](); // Expected: 1, Actual: ?
myCounters[2](); // Expected: 2, Actual: ?
```

<details>
<summary><strong>Solution</strong></summary>

**Problem:** Using `var` in the loop causes all closures to share the same `i` variable.

**Fixed Code (Solution 1 - Use `let`):**
```javascript
function makeCounters(n) {
  let counters = [];
  for (let i = 0; i < n; i++) { // 'let' creates block scope
    counters.push(function() {
      console.log(i);
    });
  }
  return counters;
}

let myCounters = makeCounters(3);
myCounters[0](); // 0
myCounters[1](); // 1
myCounters[2](); // 2
```

**Fixed Code (Solution 2 - Use IIFE):**
```javascript
function makeCounters(n) {
  let counters = [];
  for (var i = 0; i < n; i++) {
    counters.push((function(index) {
      return function() {
        console.log(index);
      };
    })(i));
  }
  return counters;
}
```

**Fixed Code (Solution 3 - Use forEach):**
```javascript
function makeCounters(n) {
  let counters = [];
  Array.from({ length: n }).forEach(function(_, i) {
    counters.push(function() {
      console.log(i);
    });
  });
  return counters;
}
```

**Explanation:** `var` has function scope, so all closures reference the same `i`. Using `let` creates a new binding for each iteration.

</details>

---

### 24. **Difficulty: Advanced** *(NEW)*
**Problem:** The `secretKeeper` below has a security flaw that allows the secret to be exposed. Identify the vulnerability and fix it.

```javascript
function secretKeeper(secret) {
  let data = { secret: secret };
  
  return {
    getData: function() {
      return data;
    },
    checkSecret: function(guess) {
      return guess === data.secret;
    }
  };
}

let keeper = secretKeeper('myPassword123');
// There's a way to access the secret here - find it and prevent it
```

<details>
<summary><strong>Solution</strong></summary>

**Problem:** The `getData()` method returns a reference to the private object, allowing mutation.

**Vulnerability:**
```javascript
let keeper = secretKeeper('myPassword123');
let myData = keeper.getData();
console.log(myData.secret); // 'myPassword123' - exposed!
myData.secret = 'hacked!';
console.log(keeper.checkSecret('myPassword123')); // false - modified!
```

**Fixed Code (Solution 1 - Return a copy):**
```javascript
function secretKeeper(secret) {
  let data = { secret: secret };
  
  return {
    getData: function() {
      // Return a copy, not the reference
      return { secret: data.secret };
      // Or freeze the copy to prevent modification
      // return Object.freeze({ secret: data.secret });
    },
    checkSecret: function(guess) {
      return guess === data.secret;
    }
  };
}
```

**Fixed Code (Solution 2 - Don't expose data at all):**
```javascript
function secretKeeper(secret) {
  // Just keep the secret as a string, not in an object
  
  return {
    checkSecret: function(guess) {
      return guess === secret;
    }
    // Don't provide getData at all
  };
}
```

**Explanation:** Returning references to mutable objects exposes private data. Either return copies or don't expose the data at all.

</details>

---

## Challenge Exercises

### 25. **Difficulty: Expert** *(NEW)*
**Problem:** Create a `makeEventEmitter` function that implements a simple event emitter with private event storage. The returned object should have methods:
- `on(eventName, callback)` - registers a callback for an event
- `off(eventName, callback)` - removes a specific callback
- `emit(eventName, ...args)` - calls all callbacks for that event with the provided arguments
- `once(eventName, callback)` - registers a callback that only fires once

```javascript
let emitter = makeEventEmitter();

function logData(data) {
  console.log('Data:', data);
}

emitter.on('data', logData);
emitter.emit('data', 'Hello'); // logs "Data: Hello"
emitter.off('data', logData);
emitter.emit('data', 'World'); // nothing happens
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeEventEmitter() {
  let events = {};
  
  return {
    on: function(eventName, callback) {
      if (!events[eventName]) {
        events[eventName] = [];
      }
      events[eventName].push(callback);
    },
    
    off: function(eventName, callback) {
      if (events[eventName]) {
        events[eventName] = events[eventName].filter(function(cb) {
          return cb !== callback;
        });
      }
    },
    
    emit: function(eventName, ...args) {
      if (events[eventName]) {
        events[eventName].forEach(function(callback) {
          callback(...args);
        });
      }
    },
    
    once: function(eventName, callback) {
      let wrapper = (...args) => {
        callback(...args);
        this.off(eventName, wrapper);
      };
      this.on(eventName, wrapper);
    }
  };
}

let emitter = makeEventEmitter();

function logData(data) {
  console.log('Data:', data);
}

emitter.on('data', logData);
emitter.emit('data', 'Hello'); // logs "Data: Hello"

emitter.once('single', (msg) => console.log('Once:', msg));
emitter.emit('single', 'First');  // logs "Once: First"
emitter.emit('single', 'Second'); // nothing happens

emitter.off('data', logData);
emitter.emit('data', 'World'); // nothing happens
```

</details>

---

### 26. **Difficulty: Expert** *(NEW)*
**Problem:** Create a `makeObservable` function that creates an observable object. Any property access or modification should be tracked privately, and you should be able to subscribe to changes.

The returned object should have:
- `set(key, value)` - sets a value and notifies subscribers
- `get(key)` - gets a value
- `subscribe(callback)` - registers a callback for any changes
- `getHistory()` - returns an array of all changes made

```javascript
let observable = makeObservable();

observable.subscribe((change) => {
  console.log(`${change.key} changed from ${change.oldValue} to ${change.newValue}`);
});

observable.set('name', 'Alice'); // triggers subscriber
observable.set('name', 'Bob');   // triggers subscriber
console.log(observable.getHistory()); // shows all changes
```

<details>
<summary><strong>Solution</strong></summary>

```javascript
function makeObservable() {
  let data = {};
  let subscribers = [];
  let history = [];
  
  return {
    set: function(key, value) {
      let oldValue = data[key];
      data[key] = value;
      
      let change = {
        key: key,
        oldValue: oldValue,
        newValue: value,
        timestamp: new Date()
      };
      
      history.push(change);
      
      // Notify all subscribers
      subscribers.forEach(function(callback) {
        callback(change);
      });
    },
    
    get: function(key) {
      return data[key];
    },
    
    subscribe: function(callback) {
      subscribers.push(callback);
      
      // Return unsubscribe function
      return function unsubscribe() {
        subscribers = subscribers.filter(function(cb) {
          return cb !== callback;
        });
      };
    },
    
    getHistory: function() {
      // Return a copy to prevent mutation
      return history.map(function(change) {
        return { ...change };
      });
    },
    
    clearHistory: function() {
      history = [];
    }
  };
}

let observable = makeObservable();

let unsubscribe = observable.subscribe((change) => {
  console.log(`${change.key} changed from ${change.oldValue} to ${change.newValue}`);
});

observable.set('name', 'Alice'); // logs change
observable.set('age', 30);       // logs change
observable.set('name', 'Bob');   // logs change

console.log(observable.get('name')); // Bob
console.log(observable.getHistory()); // Array of all changes

unsubscribe(); // Stop receiving notifications
observable.set('name', 'Charlie'); // No log output
```

</details>

---

## Key Takeaways

1. **Private data** is created using closures - inner functions maintain access to outer function variables
2. **Always return copies** of mutable objects to prevent external mutation
3. **IIFEs** create isolated scopes for modules and prevent global namespace pollution
4. **Be careful with loops** - use `let` instead of `var` to create proper closures
5. **Memory management** - be aware of closures keeping references alive
6. **Defensive programming** - assume external code will try to modify your data
7. **Use the module pattern** for organizing related private data and public APIs

---

**Total Problems: 26**
- Conceptual Questions: 7
- Coding Exercises: 12
- Debugging Exercises: 5
- Challenge Exercises: 2

Good luck with your practice!