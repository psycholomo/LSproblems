# Higher-Order Functions: Questions and Answers

## Conceptual Questions

### 1. Basic
**Question:** What are the characteristics that define higher-order functions?

**Answer:** 
Higher-order functions are functions that:
1. Take one or more functions as arguments, OR
2. Return a function as their result, OR
3. Both

Examples include `map`, `filter`, `reduce`, `forEach`, etc.

---

### 2. Basic
**Question:** Consider the code below:
```javascript
let numbers = [1, 2, 3, 4];
function checkEven(number) {
  return number % 2 === 0;
}

numbers.filter(checkEven); // [2, 4]
```
Of the two functions invoked (checkEven and filter), which is a higher-order function and why?

**Answer:**
`filter` is the higher-order function because it takes another function (`checkEven`) as an argument. `checkEven` is a regular function that is passed as a callback to `filter`.

---

## Return Value Analysis

### 3. Intermediate
**Question:** What is the return value of the filter method call below? Why?
```javascript
[1, 2, 3].filter(num => 'hi');
```

**Answer:**
The return value is `[1, 2, 3]` (all elements).

This is because the callback function returns the string `'hi'` for every element, and `'hi'` is a truthy value in JavaScript. Since the callback always returns a truthy value, `filter` includes all elements in the result array.

---

### 4. Intermediate
**Question:** What is the return value of map in the following code? Why?
```javascript
[1, 2, 3].map(num => {
  num * num;
});
```

**Answer:**
The return value is `[undefined, undefined, undefined]`.

When using curly braces `{}` without an explicit `return` statement, the function returns `undefined` by default. The expression `num * num` is evaluated but not returned.

---

### 5. Intermediate
**Question:** The following code differs slightly from the above code. What is the return value of map in this case? Why?
```javascript
[1, 2, 3].map(num => num * num);
```

**Answer:**
The return value is `[1, 4, 9]`.

When using an arrow function without curly braces, there's an implicit return. The expression `num * num` is automatically returned for each element.

---

### 6. Intermediate
**Question:** What is the callback's return value in the following code? Also, what is the return value of every in this code?
```javascript
[1, 2, 3].every(num => {
  return num = num * 2;
});
```

**Answer:**
- The callback returns `2`, `4`, and `6` respectively for each element (the assignment `num = num * 2` returns the assigned value).
- The return value of `every` is `true`.

All return values (2, 4, 6) are truthy, so `every` returns `true` since all callback invocations returned truthy values.

---

## Implementation from Scratch

### 7. Basic
**Question:** Implement execute below, such that the return values for the two function invocations match the commented values.
```javascript
function execute(func, operand) {
  // ... implement this function
}

execute(function(number) {
  return number * 2;
}, 10); // 20

execute(function(string) {
  return string.toUpperCase();
}, 'hey there buddy'); // "HEY THERE BUDDY"
```

**Answer:**
```javascript
function execute(func, operand) {
  return func(operand);
}
```

---

### 8. Intermediate
**Question:** Implement makeCheckEven below, such that the last line of the code returns an array [2, 4].
```javascript
let numbers = [1, 2, 3, 4];
function makeCheckEven() {
  // ... implement this function
}

let checkEven = makeCheckEven();

numbers.filter(checkEven); // [2, 4]
```

**Answer:**
```javascript
function makeCheckEven() {
  return function(number) {
    return number % 2 === 0;
  };
}
```

---

### 9. Intermediate
**Question:** Implement makeListTransformer below such that timesTwo's return value matches the commented return value.
```javascript
function makeListTransformer(func) {
  // ... implement this function
}

let timesTwo = makeListTransformer(function(number) {
  return number * 2;
});

timesTwo([1, 2, 3, 4]); // [2, 4, 6, 8]
```

**Answer:**
```javascript
function makeListTransformer(func) {
  return function(array) {
    return array.map(func);
  };
}
```

---

## Emulating Built-in Methods

### 10. Advanced
**Question:** Write a function that acts like the built-in Array.prototype.filter method. Your function should not mutate the input array.
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(filter(numbers, number => number > 3)); // => [ 4, 5 ]
console.log(filter(numbers, number => number < 0)); // => []
console.log(filter(numbers, () => true));           // => [ 1, 2, 3, 4, 5 ]

let values = [1, "abc", null, true, undefined, "xyz"];
console.log(filter(values, value => typeof value === "string"));
// => [ 'abc', 'xyz' ]
```

**Answer:**
```javascript
function filter(array, callback) {
  let result = [];
  for (let i = 0; i < array.length; i++) {
    if (callback(array[i], i, array)) {
      result.push(array[i]);
    }
  }
  return result;
}
```

---

### 11. Advanced
**Question:** Write a function that acts like the built-in Array.prototype.map method. Your function should not mutate the input array.
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(map(numbers, number => number * 3));  // => [ 3, 6, 9, 12, 15 ]
console.log(map(numbers, number => number + 1));  // => [ 2, 3, 4, 5, 6 ]
console.log(map(numbers, () => false));
// => [ false, false, false, false, false ]

let values = [1, "abc", null, true, undefined, "xyz"];
console.log(map(values, value => String(value)));
// => [ '1', 'abc', 'null', 'true', 'undefined', 'xyz' ]
```

**Answer:**
```javascript
function map(array, callback) {
  let result = [];
  for (let i = 0; i < array.length; i++) {
    result.push(callback(array[i], i, array));
  }
  return result;
}
```

---

### 12. Advanced
**Question:** Write a function that acts like the built-in Array.prototype.reduce method.
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(reduce(numbers, (accum, number) => accum + number));   // => 15
console.log(reduce(numbers, (prod, number) => prod * number));     // => 120
console.log(reduce(numbers, (prod, number) => prod * number, 3));  // => 360
console.log(reduce([], (accum, number) => accum + number, 10));    // => 10
```

**Answer:**
```javascript
function reduce(array, callback, initialValue) {
  let accumulator;
  let startIndex;
  
  if (initialValue === undefined) {
    accumulator = array[0];
    startIndex = 1;
  } else {
    accumulator = initialValue;
    startIndex = 0;
  }
  
  for (let i = startIndex; i < array.length; i++) {
    accumulator = callback(accumulator, array[i], i, array);
  }
  
  return accumulator;
}
```

---

## Working with Complex Data Structures

### 13. Advanced
**Question:** Given the following data structure, write some code to return a new array. The new array should contain the same sub-arrays as the original array, but each sub-array should contain only the numbers that are multiples of 3.
```javascript
let arr = [[2], [3, 5, 7], [9], [11, 15, 18]];
// Expected output: [ [], [ 3 ], [ 9 ], [ 15, 18 ] ]
```

**Answer:**
```javascript
let result = arr.map(subArr => {
  return subArr.filter(num => num % 3 === 0);
});

console.log(result); // [ [], [ 3 ], [ 9 ], [ 15, 18 ] ]
```

---

### 14. Advanced
**Question:** Given the following data structure, sort the array so that the sub-arrays are ordered based on the sum of the odd numbers that they contain.
```javascript
let arr = [[1, 6, 7], [1, 5, 3], [1, 8, 3]];
// Expected output: [ [ 1, 8, 3 ], [ 1, 6, 7 ], [ 1, 5, 3 ] ]
```

**Answer:**
```javascript
let result = arr.slice().sort((a, b) => {
  let oddSumA = a.filter(num => num % 2 === 1)
                 .reduce((sum, num) => sum + num, 0);
  let oddSumB = b.filter(num => num % 2 === 1)
                 .reduce((sum, num) => sum + num, 0);
  return oddSumA - oddSumB;
});

console.log(result); // [ [ 1, 8, 3 ], [ 1, 6, 7 ], [ 1, 5, 3 ] ]
// Odd sums: [1, 8, 3] = 4, [1, 6, 7] = 8, [1, 5, 3] = 9
```

---

### 15. Advanced
**Question:** Given the following data structure, write some code to return an array containing the colors of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.
```javascript
let obj = {
  grape: { type: 'fruit', colors: ['red', 'green'], size: 'small' },
  carrot: { type: 'vegetable', colors: ['orange'], size: 'medium' },
  apple: { type: 'fruit', colors: ['red', 'green'], size: 'medium' },
  apricot: { type: 'fruit', colors: ['orange'], size: 'medium' },
  marrow: { type: 'vegetable', colors: ['green'], size: 'large' },
};
// Expected output: [["Red", "Green"], "MEDIUM", ["Red", "Green"], ["Orange"], "LARGE"]
```

**Answer:**
```javascript
let result = Object.values(obj).map(item => {
  if (item.type === 'fruit') {
    return item.colors.map(color => color[0].toUpperCase() + color.slice(1));
  } else {
    return item.size.toUpperCase();
  }
});

console.log(result);
// [["Red", "Green"], "MEDIUM", ["Red", "Green"], ["Orange"], "LARGE"]
```

---

## Additional Advanced Questions

## Tricky Return Value & Truthiness

### 16. Advanced
**Question:** What is the return value of the following code? Explain why.
```javascript
[0, 1, 2, 3].filter(num => num);
```

**Answer:**
The return value is `[1, 2, 3]`.

The callback returns the number itself. In JavaScript, `0` is falsy, so it's filtered out. The numbers `1`, `2`, and `3` are all truthy values, so they're included in the result.

---

### 17. Advanced
**Question:** What does the following code return and why?
```javascript
['a', 'b', 'c'].map(char => char.toUpperCase());
```
Now compare it with:
```javascript
['a', 'b', 'c'].map(char => { char.toUpperCase(); });
```
What's the difference?

**Answer:**
- First version returns: `['A', 'B', 'C']` - The arrow function has an implicit return.
- Second version returns: `[undefined, undefined, undefined]` - The curly braces create a function body that requires an explicit `return` statement. Without it, the function returns `undefined`.

---

### 18. Tricky
**Question:** What is the return value of the following code?
```javascript
[1, 2, 3].reduce((acc, num) => {
  acc + num;
}, 0);
```

**Answer:**
The return value is `undefined`.

The callback function doesn't have an explicit `return` statement. The expression `acc + num` is evaluated but not returned. Since the function returns `undefined`, that becomes the accumulator for the next iteration, leading to `undefined`.

**Fixed version:**
```javascript
[1, 2, 3].reduce((acc, num) => {
  return acc + num;
}, 0); // 6

// Or with implicit return:
[1, 2, 3].reduce((acc, num) => acc + num, 0); // 6
```

---

## Closures and Higher-Order Functions

### 19. Advanced
**Question:** Implement `makeMultiplier` so that the code below works as expected:
```javascript
function makeMultiplier(multiplier) {
  // ... implement this function
}

let multiplyBy5 = makeMultiplier(5);
let multiplyBy10 = makeMultiplier(10);

console.log(multiplyBy5(3));     // 15
console.log(multiplyBy10(3));    // 30
console.log(multiplyBy5([1, 2, 3])); // [5, 10, 15]
```

**Answer:**
```javascript
function makeMultiplier(multiplier) {
  return function(value) {
    if (Array.isArray(value)) {
      return value.map(num => num * multiplier);
    }
    return value * multiplier;
  };
}
```

---

### 20. Advanced
**Question:** What will the following code output? Explain why.
```javascript
let functions = [];
for (var i = 0; i < 3; i++) {
  functions.push(() => i);
}

console.log(functions[0]()); // ?
console.log(functions[1]()); // ?
console.log(functions[2]()); // ?
```
How would you fix this to get 0, 1, 2?

**Answer:**
All three will output `3`.

This is because `var` is function-scoped, not block-scoped. All arrow functions reference the same `i` variable, which has the value `3` after the loop completes.

**Fix #1 - Use `let`:**
```javascript
let functions = [];
for (let i = 0; i < 3; i++) {  // Use 'let' instead of 'var'
  functions.push(() => i);
}
// Now outputs: 0, 1, 2
```

**Fix #2 - Use closure with IIFE:**
```javascript
let functions = [];
for (var i = 0; i < 3; i++) {
  functions.push((function(num) {
    return () => num;
  })(i));
}
// Now outputs: 0, 1, 2
```

---

## Function Composition

### 21. Advanced
**Question:** Implement a `compose` function that takes any number of functions as arguments and returns a new function that applies them from right to left.
```javascript
function compose(...funcs) {
  // ... implement this function
}

let addOne = num => num + 1;
let double = num => num * 2;
let square = num => num * num;

let compute = compose(addOne, double, square);
console.log(compute(2)); // 9 (square(2) = 4, double(4) = 8, addOne(8) = 9)
```

**Answer:**
```javascript
function compose(...funcs) {
  return function(value) {
    return funcs.reduceRight((acc, func) => func(acc), value);
  };
}

// Alternative implementation:
function compose(...funcs) {
  return function(value) {
    let result = value;
    for (let i = funcs.length - 1; i >= 0; i--) {
      result = funcs[i](result);
    }
    return result;
  };
}
```

---

### 22. Advanced
**Question:** Implement a `pipe` function (opposite of compose - applies functions left to right):
```javascript
function pipe(...funcs) {
  // ... implement this function
}

let addOne = num => num + 1;
let double = num => num * 2;
let square = num => num * num;

let compute = pipe(addOne, double, square);
console.log(compute(2)); // 36 (addOne(2) = 3, double(3) = 6, square(6) = 36)
```

**Answer:**
```javascript
function pipe(...funcs) {
  return function(value) {
    return funcs.reduce((acc, func) => func(acc), value);
  };
}
```

---

## Partial Application and Currying

### 23. Advanced
**Question:** Implement a `partial` function that allows partial application:
```javascript
function partial(func, ...fixedArgs) {
  // ... implement this function
}

function greet(greeting, name, punctuation) {
  return `${greeting}, ${name}${punctuation}`;
}

let sayHelloTo = partial(greet, 'Hello');
console.log(sayHelloTo('John', '!'));  // "Hello, John!"
console.log(sayHelloTo('Mary', '.'));  // "Hello, Mary."
```

**Answer:**
```javascript
function partial(func, ...fixedArgs) {
  return function(...remainingArgs) {
    return func(...fixedArgs, ...remainingArgs);
  };
}
```

---

### 24. Advanced
**Question:** Implement a `curry` function that transforms a multi-argument function into a sequence of single-argument functions:
```javascript
function curry(func) {
  // ... implement this function
}

function sum(a, b, c) {
  return a + b + c;
}

let curriedSum = curry(sum);
console.log(curriedSum(1)(2)(3)); // 6
console.log(curriedSum(1, 2)(3)); // 6
console.log(curriedSum(1)(2, 3)); // 6
```

**Answer:**
```javascript
function curry(func) {
  return function curried(...args) {
    if (args.length >= func.length) {
      return func(...args);
    } else {
      return function(...nextArgs) {
        return curried(...args, ...nextArgs);
      };
    }
  };
}
```

---

## Complex Transformations

### 25. Advanced
**Question:** Given the following nested data structure, write code to return a flat array of all numbers greater than 5:
```javascript
let nested = [1, [2, [3, [4, [5, [6, [7, [8]]]]]]]];
// Expected output: [6, 7, 8]
```

**Answer:**
```javascript
// Solution 1: Using flat() and filter()
let result = nested.flat(Infinity).filter(num => num > 5);

// Solution 2: Recursive approach
function flattenAndFilter(arr, threshold) {
  let result = [];
  for (let element of arr) {
    if (Array.isArray(element)) {
      result.push(...flattenAndFilter(element, threshold));
    } else if (element > threshold) {
      result.push(element);
    }
  }
  return result;
}

let result = flattenAndFilter(nested, 5);
console.log(result); // [6, 7, 8]
```

---

### 26. Advanced
**Question:** Given an array of objects representing books, write code using higher-order functions to:
1. Filter books published after 2010
2. Sort them by rating (highest first)
3. Return an array of just the titles

```javascript
let books = [
  { title: 'Book A', year: 2012, rating: 4.2 },
  { title: 'Book B', year: 2008, rating: 4.8 },
  { title: 'Book C', year: 2015, rating: 3.9 },
  { title: 'Book D', year: 2011, rating: 4.5 },
];
// Expected output: ['Book D', 'Book A', 'Book C']
```

**Answer:**
```javascript
let result = books
  .filter(book => book.year > 2010)
  .sort((a, b) => b.rating - a.rating)
  .map(book => book.title);

console.log(result); // ['Book D', 'Book A', 'Book C']
```

---

### 27. Advanced
**Question:** Implement a `groupBy` function:
```javascript
function groupBy(array, callback) {
  // ... implement this function
}

let people = [
  { name: 'Alice', age: 25 },
  { name: 'Bob', age: 30 },
  { name: 'Charlie', age: 25 },
  { name: 'David', age: 30 },
];

console.log(groupBy(people, person => person.age));
// {
//   25: [{ name: 'Alice', age: 25 }, { name: 'Charlie', age: 25 }],
//   30: [{ name: 'Bob', age: 30 }, { name: 'David', age: 30 }]
// }
```

**Answer:**
```javascript
function groupBy(array, callback) {
  return array.reduce((groups, item) => {
    let key = callback(item);
    if (!groups[key]) {
      groups[key] = [];
    }
    groups[key].push(item);
    return groups;
  }, {});
}
```

---

## Edge Cases and Gotchas

### 28. Tricky
**Question:** What's wrong with this code? How would you fix it?
```javascript
let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map(function(num) {
  setTimeout(() => num * 2, 0);
});
console.log(doubled);
```

**Answer:**
**Problem:** The callback doesn't return anything (it returns `undefined`). The `setTimeout` schedules the calculation but doesn't return its result. The result is `[undefined, undefined, undefined, undefined, undefined]`.

**Fix:**
```javascript
// If you need synchronous results:
let doubled = numbers.map(num => num * 2);

// If you really need async operations:
let promises = numbers.map(num => {
  return new Promise(resolve => {
    setTimeout(() => resolve(num * 2), 0);
  });
});

Promise.all(promises).then(doubled => {
  console.log(doubled); // [2, 4, 6, 8, 10]
});
```

---

### 29. Advanced
**Question:** What is the output of the following code?
```javascript
let arr = [1, 2, 3];
arr.map(parseInt);
```
Why doesn't it return `[1, 2, 3]`?

**Answer:**
The output is `[1, NaN, NaN]`.

**Explanation:** `map` passes three arguments to the callback: `(element, index, array)`. When you pass `parseInt` directly, it receives:
- `parseInt(1, 0, array)` → `1` (radix 0 defaults to 10)
- `parseInt(2, 1, array)` → `NaN` (radix 1 is invalid)
- `parseInt(3, 2, array)` → `NaN` (3 is not a valid digit in base 2)

**Fix:**
```javascript
arr.map(num => parseInt(num));
// or
arr.map(num => parseInt(num, 10));
```

---

### 30. Advanced
**Question:** Implement a `once` function that ensures a function can only be called once:
```javascript
function once(func) {
  // ... implement this function
}

let initialize = once(() => console.log('Initialized!'));
initialize(); // "Initialized!"
initialize(); // (nothing happens)
initialize(); // (nothing happens)
```

**Answer:**
```javascript
function once(func) {
  let called = false;
  let result;
  
  return function(...args) {
    if (!called) {
      called = true;
      result = func(...args);
    }
    return result;
  };
}
```

---

## Performance and Optimization

### 31. Advanced
**Question:** Implement a `memoize` function that caches function results:
```javascript
function memoize(func) {
  // ... implement this function
}

function slowSquare(n) {
  // Simulate slow computation
  for (let i = 0; i < 1000000000; i++) {}
  return n * n;
}

let fastSquare = memoize(slowSquare);
console.log(fastSquare(5)); // slow first time
console.log(fastSquare(5)); // instant (cached)
```

**Answer:**
```javascript
function memoize(func) {
  let cache = {};
  
  return function(...args) {
    let key = JSON.stringify(args);
    if (key in cache) {
      return cache[key];
    }
    let result = func(...args);
    cache[key] = result;
    return result;
  };
}

// More robust version using Map:
function memoize(func) {
  let cache = new Map();
  
  return function(...args) {
    let key = JSON.stringify(args);
    if (cache.has(key)) {
      return cache.get(key);
    }
    let result = func(...args);
    cache.set(key, result);
    return result;
  };
}
```

---

### 32. Advanced
**Question:** Given a large array, which approach is more efficient and why?
```javascript
// Approach A
let result = largeArray
  .filter(x => x > 10)
  .map(x => x * 2)
  .filter(x => x < 100);

// Approach B
let result = largeArray.reduce((acc, x) => {
  if (x > 10) {
    let doubled = x * 2;
    if (doubled < 100) {
      acc.push(doubled);
    }
  }
  return acc;
}, []);
```
Write a generic `transducer` function that combines multiple operations into one pass.

**Answer:**
**Approach B is more efficient** because it makes a single pass through the array, while Approach A makes three passes (filter, map, filter) and creates intermediate arrays.

**Transducer implementation:**
```javascript
function transduce(array, ...operations) {
  return array.reduce((acc, item) => {
    let value = item;
    let include = true;
    
    for (let operation of operations) {
      if (operation.type === 'filter') {
        if (!operation.fn(value)) {
          include = false;
          break;
        }
      } else if (operation.type === 'map') {
        value = operation.fn(value);
      }
    }
    
    if (include) {
      acc.push(value);
    }
    return acc;
  }, []);
}

// Usage:
let result = transduce(
  largeArray,
  { type: 'filter', fn: x => x > 10 },
  { type: 'map', fn: x => x * 2 },
  { type: 'filter', fn: x => x < 100 }
);
```

---

## Bonus Challenge

### 33. Expert
**Question:** Implement your own version of `Array.prototype.flatMap`:
```javascript
function flatMap(array, callback) {
  // ... implement this function
}

console.log(flatMap([1, 2, 3], x => [x, x * 2]));
// [1, 2, 2, 4, 3, 6]

console.log(flatMap(['hello', 'world'], str => str.split('')));
// ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
```

**Answer:**
```javascript
function flatMap(array, callback) {
  let result = [];
  for (let i = 0; i < array.length; i++) {
    let mapped = callback(array[i], i, array);
    if (Array.isArray(mapped)) {
      result.push(...mapped);
    } else {
      result.push(mapped);
    }
  }
  return result;
}

// Alternative using reduce:
function flatMap(array, callback) {
  return array.reduce((acc, item, index) => {
    let mapped = callback(item, index, array);
    return acc.concat(mapped);
  }, []);
}
```

---

### 34. Expert
**Question:** Implement a `debounce` function using higher-order function concepts:
```javascript
function debounce(func, delay) {
  // ... implement this function
}

let debouncedLog = debounce(() => console.log('Called!'), 1000);
debouncedLog(); // wait
debouncedLog(); // wait
debouncedLog(); // only this one executes after 1 second
```

**Answer:**
```javascript
function debounce(func, delay) {
  let timeoutId;
  
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  };
}

// Version that also returns a cancel method:
function debounce(func, delay) {
  let timeoutId;
  
  function debounced(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func(...args);
    }, delay);
  }
  
  debounced.cancel = function() {
    clearTimeout(timeoutId);
  };
  
  return debounced;
}
```

---

This comprehensive guide covers fundamental through expert-level concepts in higher-order functions, closures, and functional programming patterns in JavaScript!