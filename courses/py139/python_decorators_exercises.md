# Python Decorators - Practice Problems with Solutions

## 1. **Basic**: What is a decorator in Python?

### Question:
What is a decorator in Python? Explain its purpose and the syntax used to apply it to a function.

### Answer:

A **decorator** in Python is a special type of function that modifies or extends the behavior of another function without permanently changing its code. Decorators follow the principle of "wrapping" a function with additional functionality.

**Purpose of Decorators:**
- Add functionality to existing functions without modifying their code
- Implement cross-cutting concerns like logging, timing, authentication, caching
- Provide a clean, reusable way to modify function behavior
- Follow the DRY (Don't Repeat Yourself) principle

**Basic Syntax:**

```python
# Method 1: Using @ symbol (syntactic sugar)
@decorator_function
def target_function():
    pass

# Method 2: Explicit decoration (equivalent to above)
def target_function():
    pass
target_function = decorator_function(target_function)
```

**Simple Example:**

```python
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        result = func()
        print("Something after the function")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# When called:
say_hello()
# Output:
# Something before the function
# Hello!
# Something after the function
```

**Key Concepts:**
- The decorator function takes another function as an argument
- It returns a new function (usually called a "wrapper") that calls the original function
- The `@decorator` syntax is just syntactic sugar for `func = decorator(func)`

---

## 2. **Intermediate**: Decorator Order and Execution

### Question:
Consider the following two decorators and a function:

```python
from time import perf_counter
from functools import lru_cache

def time_runs(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        return_value = func(*args, **kwargs)
        print(f"The function ran in {perf_counter()-start} seconds")
        return return_value
    return wrapper

@time_runs
@lru_cache
def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True
```

Explain the order in which the decorators are applied during the function's definition and during its execution. What would be the difference in behavior if the order of the decorators was swapped?

### Answer:

**Decorator Application Order (Definition Time):**

Decorators are applied **bottom-up** (from the function outward):

```python
@time_runs      # Applied second (outer)
@lru_cache      # Applied first (inner)
def is_prime(n):
    # original function
```

This is equivalent to:
```python
is_prime = time_runs(lru_cache(is_prime))
```

**Execution Flow with Current Order:**

1. `lru_cache` is applied first, creating a cached version of `is_prime`
2. `time_runs` wraps the cached version
3. When called:
   - `time_runs` wrapper starts timing
   - Calls the cached version of `is_prime`
   - If result is cached, returns immediately (very fast)
   - If not cached, runs original function and caches result
   - `time_runs` reports the time (including cache lookup)

**Example Output:**
```python
print(is_prime(97))    # First call - runs actual computation
# The function ran in 0.0001234 seconds
# True

print(is_prime(97))    # Second call - uses cache
# The function ran in 0.0000012 seconds  # Much faster!
# True
```

**If Order Was Swapped (@lru_cache on top, @time_runs below):**

```python
@lru_cache      # Applied second (outer)
@time_runs      # Applied first (inner)
def is_prime(n):
    # original function
```

Equivalent to: `is_prime = lru_cache(time_runs(is_prime))`

**Different Behavior:**
- `time_runs` would wrap the original function first
- `lru_cache` would cache the **timed wrapper function**
- **Problem**: The timing print statement would only execute once per unique argument
- Subsequent calls with the same argument would return cached results WITHOUT timing information

**Example with Swapped Order:**
```python
print(is_prime(97))    # First call - runs computation with timing
# The function ran in 0.0001234 seconds
# True

print(is_prime(97))    # Second call - returns cached result, NO timing output
# True  (no timing message!)
```

**Key Insight:** The order matters significantly! The current order (`@time_runs` then `@lru_cache`) allows you to measure both cached and uncached performance, while the swapped order would hide timing information for cached calls.

---

## 3. **Intermediate**: Simple Logger Decorator

### Question:
Write a decorator named `simple_logger` that logs the execution of a function. It should print "Function is about to run" before the decorated function is called and "Function has finished running" after it completes. The decorator should correctly handle any arguments passed to the decorated function.

Apply this decorator to a function `greet(name)` that prints a greeting.

### Solution:

```python
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function is about to run")
        result = func(*args, **kwargs)
        print("Function has finished running")
        return result
    return wrapper

# Apply to greet function
@simple_logger
def greet(name):
    print(f"Hello, {name}!")

# Example usage:
greet("Alice")
```

**Output:**
```
Function is about to run
Hello, Alice!
Function has finished running
```

**Enhanced Version with Function Name:**

```python
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is about to run")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' has finished running")
        return result
    return wrapper

@simple_logger
def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

@simple_logger
def add_numbers(a, b):
    """Adds two numbers together."""
    return a + b

# Example usage:
greet("Bob")
print(f"Result: {add_numbers(5, 3)}")
```

**Output:**
```
Function 'greet' is about to run
Hello, Bob!
Function 'greet' has finished running
Result: Function 'add_numbers' is about to run
Function 'add_numbers' has finished running
8
```

**Version with Exception Handling:**

```python
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is about to run")
        try:
            result = func(*args, **kwargs)
            print(f"Function '{func.__name__}' has finished running successfully")
            return result
        except Exception as e:
            print(f"Function '{func.__name__}' finished with error: {e}")
            raise
    return wrapper

@simple_logger
def divide(a, b):
    return a / b

# Example usage:
print(divide(10, 2))  # Success case
# divide(10, 0)       # Error case (uncomment to test)
```

---

## 4. **Advanced**: Parameterized Repeat Decorator

### Question:
Create a parameterized decorator named `repeat`. This decorator should accept an integer argument, `times`, and make the decorated function execute that many times. The decorator should also handle any arguments passed to the decorated function.

Demonstrate its use on a function `say_hello(name)` that prints a message like `"Hello, {name}"`. For example, `@repeat(3)` should cause the function to run three times.

### Solution:

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
            return result  # Returns the result of the last execution
        return wrapper
    return decorator

# Apply to say_hello function
@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")

# Example usage:
say_hello("Alice")
```

**Output:**
```
Hello, Alice!
Hello, Alice!
Hello, Alice!
```

**Enhanced Version with Execution Counter:**

```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                print(f"Execution {i + 1}/{times}:")
                result = func(*args, **kwargs)
                results.append(result)
            return results  # Returns list of all results
        return wrapper
    return decorator

@repeat(3)
def say_hello(name):
    print(f"Hello, {name}!")
    return f"Greeted {name}"

# Example usage:
results = say_hello("Bob")
print(f"Results: {results}")
```

**Output:**
```
Execution 1/3:
Hello, Bob!
Execution 2/3:
Hello, Bob!
Execution 3/3:
Hello, Bob!
Results: ['Greeted Bob', 'Greeted Bob', 'Greeted Bob']
```

**Version with Configurable Behavior:**

```python
def repeat(times, return_all=False, show_counter=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                if show_counter:
                    print(f"[{i + 1}/{times}]", end=" ")
                result = func(*args, **kwargs)
                results.append(result)
            
            return results if return_all else results[-1]
        return wrapper
    return decorator

@repeat(3, show_counter=True)
def countdown(n):
    print(f"T-minus {n}!")
    return n

@repeat(2, return_all=True)
def get_random_number():
    import random
    num = random.randint(1, 10)
    print(f"Generated: {num}")
    return num

# Example usage:
countdown(5)
print()
numbers = get_random_number()
print(f"All generated numbers: {numbers}")
```

**Practical Example - Retry Mechanism:**

```python
def retry(times, ignore_exceptions=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if not ignore_exceptions or attempt == times - 1:
                        if attempt < times - 1:
                            print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                        else:
                            print(f"All {times} attempts failed.")
                            raise last_exception
            return None
        return wrapper
    return decorator

@retry(3, ignore_exceptions=True)
def unreliable_network_call():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return "Success!"

# Example usage (may need multiple runs to see retry behavior):
# result = unreliable_network_call()
# print(result)
```

---

## 5. **Advanced**: Preserving Function Metadata

### Question:
When creating a decorator, the metadata of the original function (like its `__name__` and `__doc__`) is often lost and replaced by the wrapper function's metadata. What function from the `functools` module can be used to prevent this, and how is it used? Provide a code example of a simple decorator that correctly preserves the original function's metadata.

### Answer:

The `functools.wraps` decorator is used to preserve the original function's metadata.

**Problem Without functools.wraps:**

```python
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

# Check metadata
print(f"Function name: {greet.__name__}")    # Output: wrapper
print(f"Function doc: {greet.__doc__}")      # Output: This is the wrapper function.
```

**Problem:** The original function's metadata is lost!

**Solution Using functools.wraps:**

```python
from functools import wraps

def simple_decorator(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        """This is the wrapper function."""
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@simple_decorator
def greet(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")

# Check metadata
print(f"Function name: {greet.__name__}")    # Output: greet
print(f"Function doc: {greet.__doc__}")      # Output: Greets a person by name.
print(f"Function module: {greet.__module__}")  # Original module preserved
```

**Complete Example with All Metadata Preserved:**

```python
from functools import wraps
import time

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)

# Metadata is preserved
print(f"Name: {calculate_fibonacci.__name__}")
print(f"Doc: {calculate_fibonacci.__doc__}")
print(f"Module: {calculate_fibonacci.__module__}")

# Function works normally
result = calculate_fibonacci(10)
print(f"Result: {result}")
```

**Advanced Example - Preserving All Attributes:**

```python
from functools import wraps

def comprehensive_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"{func.__name__} raised: {e}")
            raise
    
    # You can also manually preserve additional attributes if needed
    wrapper.__signature__ = func.__annotations__ if hasattr(func, '__annotations__') else None
    
    return wrapper

@comprehensive_decorator
def divide_numbers(a: int, b: int) -> float:
    """
    Divide two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient as a float
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    return a / b

# All metadata preserved
print(f"Name: {divide_numbers.__name__}")
print(f"Annotations: {divide_numbers.__annotations__}")
print(f"Doc: {divide_numbers.__doc__}")

# Function usage
result = divide_numbers(10, 3)
```

**Why functools.wraps is Important:**

1. **Debugging**: Error messages show the correct function name
2. **Introspection**: Tools can access original function metadata
3. **Documentation**: Help systems display original docstrings
4. **Testing**: Test frameworks can identify functions correctly
5. **Profiling**: Profilers show meaningful function names

**Best Practice:**
Always use `@wraps(func)` in your decorator wrapper functions to maintain clean, debuggable code and preserve the original function's identity and documentation.