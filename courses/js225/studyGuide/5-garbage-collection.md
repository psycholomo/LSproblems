# JavaScript Garbage Collection Questions

## Question 1
**Difficulty:** Basic

Is JavaScript a garbage-collected language, and if so, what does this entail?

<details>
<summary>Solution</summary>

JavaScript is a garbage-collected language. This means that the JS runtime, rather than the developer, handles memory deallocation.

</details>

---

## Question 2
**Difficulty:** Intermediate

Consider the code below. Is the object created and assigned to `foo` on line 2 eligible for garbage collection on line 11?

```javascript
function makeGreeting() {
  let foo = { greeting: 'hello' };
  return function(name) {
    foo.name = name;
    return foo;
  };
}

let greeting = makeGreeting();

// is the object eligible for GC here?

// more code
```

<details>
<summary>Solution</summary>

No, it is not. The closure created on the function returned by `makeGreeting` on line 9 prevents the object from being garbage collected.

</details>

---

## Question 3
**Difficulty:** Intermediate

Read the following code carefully. Will the JavaScript garbage collection mechanism garbage collect the array assigned to the variable `array` after the function `pushIt` is called on line 11?

```javascript
function makeArrays() {
  let array = [];

  return () => {
    array.push('');
    return array;
  };
}

const pushIt = makeArrays();
pushIt();
// more code
```

<details>
<summary>Solution</summary>

No. Since `pushIt` can be called multiple times, it needs to retain a reference to the `array` variable in the closure. Since `array` is never reassigned, every call to `pushIt` returns a pointer to the same array. The array gets mutated by each invocation, but it's the same array, so it is not eligible for garbage collection.

</details>

---

## Question 4
**Difficulty:** Advanced

In the following code, when can JavaScript garbage collect each of the following arrays? `[1]`, `[2]`, and `[1, 2]`.

```javascript
let a = [1];

function add(b) {
  a = a.concat(b);
}

function run() {
  let c = [2];
  let d = add(c);
}

run();
```

<details>
<summary>Solution</summary>

- We can GC `[1]` after line 4 executes. Since this line reassigns the `a` variable, `a` no longer references `[1]`, nor do any other variables in this program.
- We can GC `[2]` after the `run` function returns. Since `[2]` is only assigned to the `c` variable, `[2]` is no longer needed after `run` returns.
- We can GC `[1, 2]` only after the program ends. Since `a` is a global variable, the reference to `[1, 2]` doesn't go away until JS discards the `a` variable, and that only occurs when the program terminates.

</details>