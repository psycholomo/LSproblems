# Python Pure Functions and Side Effects - Practice Problems with Solutions

## 1. **Basic**: Essential Properties of Pure Functions

### Question:
According to the Launch School curriculum, what are the two essential properties that a function must have to be considered a "pure function"?

### Answer:

A function must have **two essential properties** to be considered pure:

1. **Deterministic**: Given the same input arguments, the function always returns the same output
2. **No Side Effects**: The function does not cause any observable changes outside of itself (no mutations, I/O operations, etc.)

**Examples:**

```python
# PURE FUNCTION - meets both criteria
def add(a, b):
    return a + b  # Always returns same result for same inputs, no side effects

# IMPURE - not deterministic
import random
def roll_dice():
    return random.randint(1, 6)  # Different output each time

# IMPURE - has side effects
def add_and_print(a, b):
    result = a + b
    print(result)  # Side effect: prints to console
    return result
```

---

## 2. **Basic**: Categories of Side Effects

### Question:
List five distinct categories of actions that cause a function call to have side effects.

### Answer:

**Five categories of side effects:**

1. **I/O Operations**: Reading from or writing to files, databases, network, console
2. **Global State Modification**: Changing global variables, class variables, or module-level state
3. **Object Mutation**: Modifying mutable objects passed as arguments (lists, dictionaries, etc.)
4. **System Interaction**: Making system calls, accessing environment variables, getting current time
5. **Exception Handling**: Raising uncaught exceptions that propagate outside the function

**Examples:**

```python
# 1. I/O Operations
def write_log(message):
    with open('log.txt', 'w') as f:  # File I/O side effect
        f.write(message)

# 2. Global State Modification
counter = 0
def increment():
    global counter
    counter += 1  # Modifies global state

# 3. Object Mutation
def append_item(lst, item):
    lst.append(item)  # Mutates the input list

# 4. System Interaction
import time
def get_current_time():
    return time.time()  # Accesses system time

# 5. Exception Handling
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")  # Raises exception
    return a / b
```

---

## 3. **Basic**: Analyzing Function Purity

### Question:
Is the following function pure? Why or why not?

```python
def add(a, b):
    return a + b
```

### Answer:

**Yes, this function is pure.**

**Reasoning:**
1. **Deterministic**: For any given inputs `a` and `b`, it always returns the same result (`a + b`)
2. **No Side Effects**: It doesn't modify any external state, perform I/O, or cause any observable changes outside the function

This is a classic example of a pure function - it simply computes and returns a value based solely on its inputs.

---

## 4. **Basic**: Identifying Side Effects

### Question:
Identify the side effect in the following function.

```python
count = 10

def countdown():
    global count
    count -= 1
    print(count)
```

### Answer:

**Two side effects:**

1. **Global State Modification**: `count -= 1` modifies the global variable `count`
2. **I/O Operation**: `print(count)` outputs to the console

**Pure version would be:**
```python
def countdown(current_count):
    return current_count - 1

# Usage:
count = 10
count = countdown(count)
print(count)  # Side effect moved outside the function
```

---

## 5. **Intermediate**: System Time and Function Purity

### Question:
Explain why a function that reads the current system time cannot be a pure function.

### Answer:

A function that reads the current system time **violates the deterministic property** of pure functions.

**Reasoning:**
- **Non-deterministic**: Each call returns a different value (the current time)
- **External dependency**: The function depends on system state (the system clock)
- **Same inputs, different outputs**: Even with no input parameters, consecutive calls produce different results

**Example:**
```python
import time

def get_current_time():
    return time.time()

# These calls return different values
print(get_current_time())  # 1698765432.123
time.sleep(1)
print(get_current_time())  # 1698765433.456 - Different!
```

**Pure alternative for time-based operations:**
```python
def format_timestamp(timestamp):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))

# Usage: pass timestamp as parameter
current_time = time.time()  # Side effect happens outside
formatted = format_timestamp(current_time)  # Pure function
```

---

## 6. **Intermediate**: Multiple Side Effects Analysis

### Question:
What are all the side effects present in the foo function in the following code?

```python
bar = 42
qux = [1, 2, 3]

def foo(lst):
    value = lst.pop()
    print(f'popped {value} from the list')
    return value + bar

foo(qux)
```

### Answer:

**Two side effects:**

1. **Object Mutation**: `lst.pop()` modifies the input list by removing the last element
2. **I/O Operation**: `print(f'popped {value} from the list')` outputs to the console

**Demonstration:**
```python
bar = 42
qux = [1, 2, 3]

print("Before:", qux)  # [1, 2, 3]
result = foo(qux)
print("After:", qux)   # [1, 2] - list was modified!
print("Result:", result)  # 45 (3 + 42)
```

**Pure version:**
```python
def foo_pure(lst, bar_value):
    if not lst:
        raise ValueError("List cannot be empty")
    return lst[-1] + bar_value  # No mutation, no printing

# Usage:
bar = 42
qux = [1, 2, 3]
result = foo_pure(qux, bar)
print(f'Would pop {qux[-1]} from the list')  # Side effect outside function
print("List unchanged:", qux)  # [1, 2, 3]
```

---

## 7. **Intermediate**: Exception Handling and Purity

### Question:
Is the following function find_max a pure function? Explain your reasoning.

```python
def find_max(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return max(numbers)
```

### Answer:

**This is a borderline case, but generally considered impure** due to the exception.

**Arguments for impurity:**
- **Side Effect**: Raising an uncaught exception is considered a side effect because it changes the program's control flow
- **Observable Effect**: The exception can be caught and handled outside the function

**Arguments for purity:**
- **Deterministic**: Same input always produces the same result (value or exception)
- **No External Mutation**: Doesn't modify external state

**Pure alternative:**
```python
def find_max_pure(numbers):
    if not numbers:
        return None  # Or return a tuple (success, value)
    return max(numbers)

# Or using Optional/Result pattern
from typing import Optional

def find_max_safe(numbers) -> Optional[int]:
    return max(numbers) if numbers else None
```

**Industry perspective**: Many consider functions that raise exceptions as having side effects, making them technically impure, even though they're deterministic.

---

## 8. **Intermediate**: Refactoring for Purity

### Question:
The update_record function below has a side effect. Identify the side effect and rewrite the function to be pure, returning a new dictionary with the updated value instead of modifying the original.

```python
# Impure function
def update_record(record, key, value):
    record[key] = value
```

### Answer:

**Side effect**: The function mutates the input dictionary `record`.

**Pure version:**
```python
def update_record_pure(record, key, value):
    """
    Returns a new dictionary with the updated key-value pair.
    Original dictionary remains unchanged.
    """
    new_record = record.copy()
    new_record[key] = value
    return