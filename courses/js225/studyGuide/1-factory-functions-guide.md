# Factory Functions - Practice Problems & Answer Key

## Conceptual Questions

### 1. Basic: What are the main advantages of using factory functions for object creation in JavaScript?

**Answer:**
- **Simple and flexible**: Easy to understand and use, no need for `new` keyword
- **Encapsulation**: Can create private variables using closures
- **Easy composition**: Can easily combine multiple factory functions or mix in functionality
- **No confusion with `this`**: Avoid issues with forgetting to use `new` or losing context
- **Dynamic object creation**: Can conditionally add properties/methods based on arguments
- **Works well with functional programming**: Fits naturally into functional programming patterns

---

### 2. Basic: What are two disadvantages of working with factory functions?

**Answer:**
1. **Memory inefficiency**: Each object gets its own copy of all methods, rather than sharing them through a prototype. This uses more memory when creating many objects.
2. **No clear type/identity**: Objects created by factory functions don't have a specific constructor type. You can't use `instanceof` to check what factory created them, making it harder to identify object types.

---

### 3. Intermediate: Explain why objects created by factory functions are said to not have a specific "type". How does this affect the use of instanceof and the constructor property on these objects?

**Answer:**

Objects from factory functions don't have a specific type because they're just plain objects created with `{}` or `Object.create()`. They don't have a constructor function associated with them in the way that constructor functions or classes do.

```javascript
function makeDog(name) {
  return {
    name: name,
    bark() { console.log('Woof!'); }
  };
}

function Dog(name) {
  this.name = name;
}

let factoryDog = makeDog('Buddy');
let constructorDog = new Dog('Max');

// instanceof doesn't work with factory functions
console.log(constructorDog instanceof Dog);  // true
console.log(factoryDog instanceof makeDog);  // false - makeDog is not a constructor

// constructor property
console.log(constructorDog.constructor === Dog);    // true
console.log(factoryDog.constructor === makeDog);    // false
console.log(factoryDog.constructor === Object);     // true - just a plain object
```

**Impact:**
- Can't use `instanceof` to check what factory created an object
- Can't easily identify or group objects by their "type"
- Makes debugging and type-checking more difficult
- Harder to determine what factory function created a particular object

---

### 4. Intermediate: A colleague argues that factory functions are not ideal because every object created gets its own copy of all methods, potentially using more memory. Explain this disadvantage with a code example and describe a scenario where this might not be a significant concern.

**Answer:**

**The Problem:**

```javascript
// Factory function - each object gets its own copy of methods
function createDog(name) {
  return {
    name: name,
    bark() {
      console.log(this.name + ' barks!');
    },
    eat() {
      console.log(this.name + ' eats!');
    }
  };
}

let dog1 = createDog('Buddy');
let dog2 = createDog('Max');

// Each dog has its own bark and eat methods
console.log(dog1.bark === dog2.bark);  // false - different functions!

// Compared to constructor pattern with shared methods
function Dog(name) {
  this.name = name;
}

Dog.prototype.bark = function() {
  console.log(this.name + ' barks!');
};

let dog3 = new Dog('Rex');
let dog4 = new Dog('Spot');

console.log(dog3.bark === dog4.bark);  // true - same function shared via prototype!
```

**When this might NOT be a significant concern:**

1. **Small number of objects**: If you're only creating a handful of objects (e.g., 5-10), the memory overhead is negligible in modern applications.

2. **Small, simple methods**: If the methods are tiny (a few lines), the memory difference is minimal.

3. **Need for private data**: When you need true private variables via closures, the trade-off is worth it:
   ```javascript
   function createBankAccount(initialBalance) {
     let balance = initialBalance;  // Private!
     
     return {
       deposit(amount) { balance += amount; },
       getBalance() { return balance; }
     };
   }
   ```

4. **Objects with different behavior**: If each object needs genuinely different implementations of methods based on initialization parameters.

5. **Modern hardware**: With today's memory capacities, unless you're creating thousands of objects, the difference is often imperceptible.

---

### 5. Advanced: Based on their advantages and disadvantages, describe two scenarios: one where using an object factory is an excellent choice, and one where another object creation pattern (like constructors or classes) would be more appropriate.

**Answer:**

**Scenario 1: Factory Functions Are Excellent**

**Use Case: Configuration Objects or Service Managers with Private State**

```javascript
function createAPIClient(apiKey) {
  let requestCount = 0;  // Private variable
  const baseURL = 'https://api.example.com';
  
  // Private function
  function logRequest() {
    requestCount++;
    console.log(`Request #${requestCount}`);
  }
  
  return {
    get(endpoint) {
      logRequest();
      return fetch(`${baseURL}${endpoint}`, {
        headers: { 'Authorization': `Bearer ${apiKey}` }
      });
    },
    post(endpoint, data) {
      logRequest();
      return fetch(`${baseURL}${endpoint}`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${apiKey}` },
        body: JSON.stringify(data)
      });
    },
    getRequestCount() {
      return requestCount;  // Read-only access to private data
    }
  };
}

let client = createAPIClient('secret-key-123');
// Can't access apiKey or requestCount directly - truly private!
```

**Why factory functions are ideal here:**
- Need for true private data (apiKey, requestCount)
- Only creating one or a few instances
- Don't need type identification
- Encapsulation is more important than memory efficiency

---

**Scenario 2: Constructors/Classes Are More Appropriate**

**Use Case: Creating Many Game Entities (Players, Enemies, NPCs)**

```javascript
class Enemy {
  constructor(name, health, damage) {
    this.name = name;
    this.health = health;
    this.damage = damage;
    this.isAlive = true;
  }
  
  attack(target) {
    target.takeDamage(this.damage);
  }
  
  takeDamage(amount) {
    this.health -= amount;
    if (this.health <= 0) {
      this.isAlive = false;
      this.die();
    }
  }
  
  die() {
    console.log(`${this.name} has been defeated!`);
  }
}

class Boss extends Enemy {
  constructor(name, health, damage, specialAbility) {
    super(name, health, damage);
    this.specialAbility = specialAbility;
  }
  
  useSpecialAbility() {
    console.log(`${this.name} uses ${this.specialAbility}!`);
  }
}

// Creating hundreds of enemies in a game
let enemies = [];
for (let i = 0; i < 100; i++) {
  enemies.push(new Enemy(`Goblin ${i}`, 50, 10));
}
```

**Why constructors/classes are ideal here:**
- Creating many instances (memory efficiency matters)
- Need inheritance (Boss extends Enemy)
- Want to use `instanceof` for type checking (e.g., `enemy instanceof Boss`)
- Methods are the same for all instances (should be shared)
- Don't need private data (game state is typically public for simplicity)

---

## Coding & Refactoring Exercises

### 6. Basic: Rewrite the code to use object-literal syntax

**Original Code:**
```javascript
function makeObj() {
  let obj = {};
  obj.propA = 10;
  obj.propB = 20;
  return obj;
}
```

**Answer:**
```javascript
function makeObj() {
  return {
    propA: 10,
    propB: 20
  };
}
```

---

### 7. Basic: Where is there duplication? How could a factory function help?

**Answer:**

**Duplication identified:**
- The structure of all three objects is identical
- The `getDescription` method has the same implementation in all three
- Only the `name` and `continent` values differ

**How a factory function helps:**

```javascript
function makeCountry(name, continent) {
  return {
    name: name,
    continent: continent,
    getDescription() {
      return this.name + ' is located in ' + this.continent + '.';
    }
  };
}

let chile = makeCountry('The Republic of Chile', 'South America');
let canada = makeCountry('Canada', 'North America');
let southAfrica = makeCountry('The Republic of South Africa', 'Africa');
```

**Benefits:**
- No code duplication
- Single source of truth for the object structure
- Easy to add new properties/methods to all countries
- Easy to create new country objects

---

### 8. Intermediate: Implement makeCountry factory function

**Answer:**
```javascript
function makeCountry(name, continent) {
  return {
    name: name,
    continent: continent,
    getDescription() {
      return this.name + ' is located in ' + this.continent + '.';
    }
  };
}

// Test
let chile = makeCountry('The Republic of Chile', 'South America');
let canada = makeCountry('Canada', 'North America');
let southAfrica = makeCountry('The Republic of South Africa', 'Africa');

console.log(chile.getDescription());       // "The Republic of Chile is located in South America."
console.log(canada.getDescription());      // "Canada is located in North America."
console.log(southAfrica.getDescription()); // "The Republic of South Africa is located in Africa."
```

---

### 9. Intermediate: Add visited property with default value false

**Answer:**
```javascript
function makeCountry(name, continent) {
  return {
    name: name,
    continent: continent,
    visited: false,
    getDescription() {
      return this.name + ' is located in ' + this.continent + '.';
    }
  };
}
```

---

### 10. Intermediate: Accept optional third argument for visited

**Answer:**
```javascript
function makeCountry(name, continent, visited) {
  return {
    name: name,
    continent: continent,
    visited: visited !== undefined ? visited : false,
    getDescription() {
      return this.name + ' is located in ' + this.continent + '.';
    }
  };
}

// Alternative using default parameter
function makeCountry(name, continent, visited = false) {
  return {
    name: name,
    continent: continent,
    visited: visited,
    getDescription() {
      return this.name + ' is located in ' + this.continent + '.';
    }
  };
}

// Test
let chile = makeCountry('The Republic of Chile', 'South America');
console.log(chile.visited);  // false

let canada = makeCountry('Canada', 'North America', true);
console.log(canada.visited);  // true
```

---

### 11. Intermediate: Create createPlayer factory function

**Answer:**
```javascript
function createPlayer(name, level) {
  return {
    name: name,
    level: level,
    attack() {
      console.log(`${this.name} attacks!`);
    },
    levelUp() {
      this.level += 1;
    }
  };
}

// Test
let player1 = createPlayer('Warrior', 1);
player1.attack();      // "Warrior attacks!"
console.log(player1.level);  // 1
player1.levelUp();
console.log(player1.level);  // 2
```

---

### 12. Intermediate: Create createInvoice factory function

**Answer:**
```javascript
function createInvoice(services) {
  services = services || {};
  
  return {
    phone: services.phone !== undefined ? services.phone : 3000,
    internet: services.internet !== undefined ? services.internet : 5500,
    total() {
      return this.phone + this.internet;
    }
  };
}

// Alternative using default parameters and destructuring
function createInvoice(services = {}) {
  let phone = services.phone !== undefined ? services.phone : 3000;
  let internet = services.internet !== undefined ? services.internet : 5500;
  
  return {
    phone: phone,
    internet: internet,
    total() {
      return this.phone + this.internet;
    }
  };
}

function invoiceTotal(invoices) {
  let total = 0;
  let i;

  for (i = 0; i < invoices.length; i += 1) {
    total += invoices[i].total();
  }

  return total;
}

let invoices = [];
invoices.push(createInvoice());
invoices.push(createInvoice({ internet: 6500 }));
invoices.push(createInvoice({ phone: 2000 }));
invoices.push(createInvoice({ phone: 1000, internet: 4500 }));

console.log(invoiceTotal(invoices)); // => 31000
// Breakdown: 8500 + 10000 + 7500 + 5000 = 31000
```

---

### 13. Advanced: Create createPayment factory function

**Answer:**
```javascript
function createPayment(services) {
  services = services || {};
  
  return {
    phone: services.phone || 0,
    internet: services.internet || 0,
    total() {
      return this.phone + this.internet;
    }
  };
}

// Test
let invoice = createInvoice({ phone: 1200, internet: 4000 });
let payment1 = createPayment({ internet: 2000 });
let payment2 = createPayment({ phone: 1000 });
let payment3 = createPayment();

function amountDue(invoice) {
  let totalPayments = payment1.total() + payment2.total() + payment3.total();
  return invoice.total() - totalPayments;
}

console.log(amountDue(invoice));  // 2200
// Invoice total: 1200 + 4000 = 5200
// Payments: 2000 + 1000 + 0 = 3000
// Due: 5200 - 3000 = 2200
```

---

### 14. Advanced: Create createItem factory function

**Answer:**
```javascript
function createItem(name, category, price) {
  return {
    name: name,
    category: category,
    price: price,
    details() {
      console.log(`${this.name} (${this.category}): $${this.price.toFixed(2)}`);
    }
  };
}

// Test
let apple = createItem('Apple', 'Fruit', 1.50);
apple.details();  // "Apple (Fruit): $1.50"

let bread = createItem('Whole Wheat Bread', 'Bakery', 3.99);
bread.details();  // "Whole Wheat Bread (Bakery): $3.99"
```

---

### 15. Advanced: Create createShoppingCart factory function

**Answer:**
```javascript
function createShoppingCart() {
  return {
    items: [],
    
    addItem(item) {
      this.items.push(item);
    },
    
    calculateTotal() {
      return this.items.reduce((sum, item) => sum + item.price, 0);
    },
    
    checkout() {
      let total = this.calculateTotal();
      console.log(`Total: $${total.toFixed(2)}`);
      this.items = [];
    }
  };
}

// Test
let cart = createShoppingCart();
let apple = createItem('Apple', 'Fruit', 1.50);
let bread = createItem('Whole Wheat Bread', 'Bakery', 3.99);
let milk = createItem('Milk', 'Dairy', 2.99);

cart.addItem(apple);
cart.addItem(bread);
cart.addItem(milk);

console.log(cart.calculateTotal());  // 8.48
cart.checkout();  // "Total: $8.48"
console.log(cart.items.length);  // 0
```

---

## Additional Advanced Problems

### 16. Advanced: Private State with Counter

Create a factory function `createCounter` that returns an object with:
- A `count` variable that starts at 0 and is **truly private** (cannot be accessed directly)
- An `increment()` method that increases the count by 1 and returns the new value
- A `decrement()` method that decreases the count by 1 and returns the new value
- A `reset()` method that sets count back to 0
- A `getValue()` method that returns the current count

The key requirement: there should be **no way** to directly modify or access the `count` variable from outside the returned object.

**Answer:**
```javascript
function createCounter() {
  let count = 0;  // Private variable via closure
  
  return {
    increment() {
      count += 1;
      return count;
    },
    
    decrement() {
      count -= 1;
      return count;
    },
    
    reset() {
      count = 0;
    },
    
    getValue() {
      return count;
    }
  };
}

// Test
let counter = createCounter();
console.log(counter.getValue());  // 0
console.log(counter.increment()); // 1
console.log(counter.increment()); // 2
console.log(counter.decrement()); // 1
counter.reset();
console.log(counter.getValue());  // 0

// Trying to access count directly doesn't work
console.log(counter.count);  // undefined
counter.count = 100;  // This creates a new property, doesn't affect the private count
console.log(counter.getValue());  // Still 0, private count is unchanged
```

---

### 17. Advanced: Composing Factory Functions

Create three factory functions that can be composed together:

1. `createWalker()` - returns an object with a `walk()` method that logs "Walking..."
2. `createSwimmer()` - returns an object with a `swim()` method that logs "Swimming..."
3. `createFlyer()` - returns an object with a `fly()` method that logs "Flying..."

Then create a `createDuck` factory function that uses these three factories to create a duck that can walk, swim, and fly. The duck should also have a `name` property.

**Answer:**
```javascript
function createWalker() {
  return {
    walk() {
      console.log('Walking...');
    }
  };
}

function createSwimmer() {
  return {
    swim() {
      console.log('Swimming...');
    }
  };
}

function createFlyer() {
  return {
    fly() {
      console.log('Flying...');
    }
  };
}

function createDuck(name) {
  return {
    name: name,
    ...createWalker(),
    ...createSwimmer(),
    ...createFlyer()
  };
}

// Alternative using Object.assign
function createDuck(name) {
  return Object.assign(
    { name: name },
    createWalker(),
    createSwimmer(),
    createFlyer()
  );
}

// Test
let duck = createDuck('Donald');
console.log(duck.name);  // "Donald"
duck.walk();  // "Walking..."
duck.swim();  // "Swimming..."
duck.fly();   // "Flying..."

// Now create other animals with different combinations
function createPenguin(name) {
  return Object.assign(
    { name: name },
    createWalker(),
    createSwimmer()
    // No flying!
  );
}

let penguin = createPenguin('Pingu');
penguin.walk();  // "Walking..."
penguin.swim();  // "Swimming..."
// penguin.fly();  // undefined - penguins can't fly!
```

---

### 18. Advanced: Factory with Validation

Create a factory function `createUser` that accepts `username`, `email`, and `age` as arguments. The factory should:

1. Validate that:
   - `username` is at least 3 characters long
   - `email` contains an '@' symbol
   - `age` is a number between 13 and 120

2. If validation fails, return `null` instead of creating the user

3. If validation passes, return an object with:
   - The three properties
   - A `getInfo()` method that returns a formatted string
   - A `updateEmail(newEmail)` method that validates and updates the email

**Answer:**
```javascript
function createUser(username, email, age) {
  // Validation
  if (username.length < 3) {
    console.log('Error: Username must be at least 3 characters');
    return null;
  }
  
  if (!email.includes('@')) {
    console.log('Error: Email must contain @');
    return null;
  }
  
  if (typeof age !== 'number' || age < 13 || age > 120) {
    console.log('Error: Age must be a number between 13 and 120');
    return null;
  }
  
  // Create user object
  return {
    username: username,
    email: email,
    age: age,
    
    getInfo() {
      return `${this.username} (${this.age}): ${this.email}`;
    },
    
    updateEmail(newEmail) {
      if (!newEmail.includes('@')) {
        console.log('Error: Invalid email format');
        return false;
      }
      this.email = newEmail;
      return true;
    }
  };
}

// Test
let user1 = createUser('john_doe', 'john@example.com', 25);
console.log(user1.getInfo());  // "john_doe (25): john@example.com"

let user2 = createUser('jo', 'invalid', 25);  // Error: Username must be at least 3 characters
console.log(user2);  // null

let user3 = createUser('jane', 'invalid-email', 25);  // Error: Email must contain @
console.log(user3);  // null

let user4 = createUser('jane', 'jane@example.com', 200);  // Error: Age must be between 13 and 120
console.log(user4);  // null

// Test updateEmail
user1.updateEmail('newemail@example.com');
console.log(user1.getInfo());  // "john_doe (25): newemail@example.com"

user1.updateEmail('invalid');  // Error: Invalid email format
```

---

### 19. Advanced: Bank Account with Transaction History

Create a factory function `createBankAccount` that creates a bank account with:

1. A private `balance` that starts at an initial amount
2. A private `transactions` array that tracks all deposits and withdrawals
3. Methods:
   - `deposit(amount)` - adds to balance and records the transaction
   - `withdraw(amount)` - subtracts from balance (if sufficient funds) and records the transaction
   - `getBalance()` - returns the current balance
   - `getTransactionHistory()` - returns a copy of the transactions array (not the original!)
   - `printStatement()` - logs all transactions in a formatted way

Each transaction should be an object with: `{ type: 'deposit' or 'withdraw', amount: number, date: Date, balanceAfter: number }`

**Answer:**
```javascript
function createBankAccount(initialBalance) {
  let balance = initialBalance;
  let transactions = [];
  
  function recordTransaction(type, amount) {
    transactions.push({
      type: type,
      amount: amount,
      date: new Date(),
      balanceAfter: balance
    });
  }
  
  return {
    deposit(amount) {
      if (amount <= 0) {
        console.log('Error: Deposit amount must be positive');
        return false;
      }
      balance += amount;
      recordTransaction('deposit', amount);
      console.log(`Deposited $${amount}. New balance: $${balance}`);
      return true;
    },
    
    withdraw(amount) {
      if (amount <= 0) {
        console.log('Error: Withdrawal amount must be positive');
        return false;
      }
      if (amount > balance) {
        console.log('Error: Insufficient funds');
        return false;
      }
      balance -= amount;
      recordTransaction('withdraw', amount);
      console.log(`Withdrew $${amount}. New balance: $${balance}`);
      return true;
    },
    
    getBalance() {
      return balance;
    },
    
    getTransactionHistory() {
      // Return a copy to prevent external modification
      return transactions.map(t => ({ ...t }));
    },
    
    printStatement() {
      console.log('\n--- Account Statement ---');
      console.log(`Current Balance: $${balance}\n`);
      
      if (transactions.length === 0) {
        console.log('No transactions yet.');
        return;
      }
      
      transactions.forEach((transaction, index) => {
        let sign = transaction.type === 'deposit' ? '+' : '-';
        console.log(
          `${index + 1}. ${transaction.date.toLocaleDateString()} - ` +
          `${transaction.type.toUpperCase()}: ${sign}$${transaction.amount} ` +
          `(Balance: $${transaction.balanceAfter})`
        );
      });
      console.log('--- End Statement ---\n');
    }
  };
}

// Test
let account = createBankAccount(1000);
console.log(account.getBalance());  // 1000

account.deposit(500);   // "Deposited $500. New balance: $1500"
account.withdraw(200);  // "Withdrew $200. New balance: $1300"
account.withdraw(2000); // "Error: Insufficient funds"
account.deposit(100);   // "Deposited $100. New balance: $1400"

account.printStatement();

// Try to access private data
console.log(account.balance);  // undefined
console.log(account.transactions);  // undefined

// Get transaction history (should be a copy)
let history = account.getTransactionHistory();
history[0].amount = 99999;  // Modifying the copy
console.log(account.getTransactionHistory()[0].amount);  // Original unchanged
```

---

### 20. Expert: Todo List Manager with Categories

Create a factory function `createTodoManager` that manages todos with categories. It should have:

1. Private data structures for todos and categories
2. Methods:
   - `addCategory(name)` - adds a category
   - `addTodo(title, categoryName)` - adds a todo to a category
   - `completeTodo(title)` - marks a todo as complete
   - `getTodosByCategory(categoryName)` - returns all todos in that category
   - `getIncompleteTodos()` - returns all incomplete todos across all categories
   - `deleteTodo(title)` - removes a todo
   - `printSummary()` - prints a nice summary of all categories and their todos

Each todo should have: `{ title, category, completed, createdAt }`

**Answer:**
```javascript
function createTodoManager() {
  let categories = new Set();
  let todos = [];
  
  return {
    addCategory(name) {
      if (categories.has(name)) {
        console.log(`Category "${name}" already exists`);
        return false;
      }
      categories.add(name);
      console.log(`Category "${name}" added`);
      return true;
    },
    
    addTodo(title, categoryName) {
      if (!categories.has(categoryName)) {
        console.log(`Error: Category "${categoryName}" does not exist`);
        return false;
      }
      
      // Check if todo with same title already exists
      if (todos.find(todo => todo.title === title)) {
        console.log(`Error: Todo "${title}" already exists`);
        return false;
      }
      
      todos.push({
        title: title,
        category: categoryName,
        completed: false,
        createdAt: new Date()
      });
      console.log(`Todo "${title}" added to ${categoryName}`);
      return true;
    },
    
    completeTodo(title) {
      let todo = todos.find(t => t.title === title);
      if (!todo) {
        console.log(`Error: Todo "${title}" not found`);
        return false;
      }
      todo.completed = true;
      console.log(`Todo "${title}" marked as complete`);
      return true;
    },
    
    getTodosByCategory(categoryName) {
      return todos
        .filter(todo => todo.category === categoryName)
        .map(todo => ({ ...todo }));  // Return copies
    },
    
    getIncompleteTodos() {
      return todos
        .filter(todo => !todo.completed)
        .map(todo => ({ ...todo }));
    },
    
    deleteTodo(title) {
      let index = todos.findIndex(t => t.title === title);
      if (index === -1) {
        console.log(`Error: Todo "${title}" not found`);
        return false;
      }
      todos.splice(index, 1);
      console.log(`Todo "${title}" deleted`);
      return true;
    },
    
    printSummary() {
      console.log('\n=== TODO SUMMARY ===\n');
      
      let categoriesArray = Array.from(categories);
      
      if (categoriesArray.length === 0) {
        console.log('No categories yet.');
        return;
      }
      
      categoriesArray.forEach(category => {
        let categoryTodos = todos.filter(t => t.category === category);
        let completed = categoryTodos.filter(t => t.completed).length;
        let total = categoryTodos.length;
        
        console.log(`📁 ${category} (${completed}/${total} complete)`);
        
        if (categoryTodos.length === 0) {
          console.log('   No todos in this category\n');
        } else {
          categoryTodos.forEach(todo => {
            let checkbox = todo.completed ? '☑' : '☐';
            console.log(`   ${checkbox} ${todo.title}`);
          });
          console.log();
        }
      });
      
      console.log('===================\n');
    }
  };
}

// Test
let manager = createTodoManager();

manager.addCategory('Work');
manager.addCategory('Personal');
manager.addCategory('Shopping');

manager.addTodo('Finish project', 'Work');
manager.addTodo('Reply to emails', 'Work');
manager.addTodo('Call mom', 'Personal');
manager.addTodo('Buy groceries', 'Shopping');
manager.addTodo('Buy birthday gift', 'Shopping');

manager.completeTodo('Call mom');
manager.completeTodo('Buy groceries');

manager.printSummary();

console.log('Incomplete todos:');
console.log(manager.getIncompleteTodos());

manager.deleteTodo('Reply to emails');
manager.printSummary();
```

---

### 21. Expert: Event Emitter

Create a factory function `createEventEmitter` that implements a simple event emitter pattern. It should have:

1. `on(eventName, callback)` - registers a callback for an event
2. `off(eventName, callback)` - removes a specific callback for an event
3. `emit(eventName, ...args)` - calls all callbacks registered for that event with the provided arguments
4. `once(eventName, callback)` - registers a callback that only fires once, then removes itself
5. `listenerCount(eventName)` - returns the number of listeners for an event

All event listeners should be stored privately.

**Answer:**
```javascript
function createEventEmitter() {
  let events = {};  // Private storage for event listeners
  
  return {
    on(eventName, callback) {
      if (typeof callback !== 'function') {
        console.log('Error: Callback must be a function');
        return;
      }
      
      if (!events[eventName]) {
        events[eventName] = [];
      }
      
      events[eventName].push(callback);
    },
    
    off(eventName, callback) {
      if (!events[eventName]) {
        return;
      }
      
      events[eventName] = events[eventName].filter(cb => cb !== callback);
      
      // Clean up if no listeners left
      if (events[eventName].length === 0) {
        delete events[eventName];
      }
    },
    
    emit(eventName, ...args) {
      if (!events[eventName]) {
        return;
      }
      
      // Create a copy to avoid issues if a listener removes itself
      let listeners = [...events[eventName]];
      
      listeners.forEach(callback => {
        callback(...args);
      });
    },
    
    once(eventName, callback) {
      if (typeof callback !== 'function') {
        console.log('Error: Callback must be a function');
        return;
      }
      
      // Create a wrapper function that removes itself after being called
      let wrapper = (...args) => {
        callback(...args);
        this.off(eventName, wrapper);
      };
      
      this.on(eventName, wrapper);
    },
    
    listenerCount(eventName) {
      return events[eventName] ? events[eventName].length : 0;
    }
  };
}

// Test
let emitter = createEventEmitter();

// Regular listeners
function onUserLogin(username) {
  console.log(`${username} logged in`);
}

function sendWelcomeEmail(username) {
  console.log(`Sending welcome email to ${username}`);
}

emitter.on('login', onUserLogin);
emitter.on('login', sendWelcomeEmail);

console.log(emitter.listenerCount('login'));  // 2

emitter.emit('login', 'john_doe');
// "john_doe logged in"
// "Sending welcome email to john_doe"

// Once listener
emitter.once('firstVisit', (username) => {
  console.log(`Welcome for the first time, ${username}!`);
});

emitter.emit('firstVisit', 'jane_doe');  // "Welcome for the first time, jane_doe!"
emitter.emit('firstVisit', 'jane_doe');  // Nothing happens (listener removed)

// Remove listener
emitter.off('login', sendWelcomeEmail);
console.log(emitter.listenerCount('login'));  // 1

emitter.emit('login', 'bob');  // Only "bob logged in" (email sender removed)
```

---

## Summary

These problems progressively introduce:
- Basic factory function syntax and patterns
- Handling optional parameters and defaults
- Object composition and code reuse
- Private state using closures
- Validation and error handling
- Complex state management
- Advanced patterns like event emitters

The key concepts tested are:
1. Understanding when and why to use factory functions
2. Creating objects with methods
3. Using closures for privacy
4. Composing multiple factories
5. Managing complex internal state
6. Implementing real-world patterns