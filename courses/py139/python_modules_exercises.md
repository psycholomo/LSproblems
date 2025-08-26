# Python Modules - Practice Problems with Solutions

## 1. **Basic**: What is a Module in Python?

### Question:
What is a module in Python? According to the Launch School curriculum, what are the two primary roles that modules serve?

### Answer:

A **module** in Python is a file containing Python code that can define functions, classes, and variables, and can also include runnable code. Modules are identified by their `.py` file extension and serve as a way to organize and reuse code.

**Two Primary Roles of Modules:**

1. **Code Organization and Namespace Management**
   - Modules help organize related code into separate files
   - They create separate namespaces to avoid naming conflicts
   - They make code more maintainable and structured

2. **Code Reusability**
   - Modules allow code to be written once and used multiple times
   - They can be imported and used in different programs
   - They promote the DRY (Don't Repeat Yourself) principle

**Example:**
```python
# math_operations.py (module)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159

# main.py (using the module)
import math_operations

result1 = math_operations.add(5, 3)
result2 = math_operations.multiply(4, 2)
print(f"PI value: {math_operations.PI}")
```

**Benefits of Using Modules:**
- **Maintainability**: Easier to manage large codebases
- **Reusability**: Share code across multiple projects
- **Namespace separation**: Avoid naming conflicts
- **Modularity**: Break complex programs into manageable pieces

---

## 2. **Intermediate**: Namespace Pollution

### Question:
Explain what "namespace pollution" is in the context of Python modules. Which type of import statement is most likely to cause it, and why is it generally discouraged?

### Answer:

**Namespace Pollution** occurs when importing modules introduces too many names into the current namespace, potentially causing naming conflicts and making code harder to understand and maintain.

**Import Statement Most Likely to Cause It:**
The `from module import *` statement (wildcard import) is most likely to cause namespace pollution.

**Why It's Problematic:**

```python
# BAD: Wildcard import causes namespace pollution
from math import *
from statistics import *

# Now your namespace is polluted with dozens of names
print(sin(1))     # Where does 'sin' come from? Not clear!
print(mean([1,2,3]))  # Where does 'mean' come from?

# What if both modules have a function with the same name?
# The second import will overwrite the first!
```

**Problems with Wildcard Imports:**

1. **Unclear Origin**: Hard to tell which module a function comes from
2. **Name Conflicts**: Functions from different modules might have the same name
3. **Hidden Dependencies**: Not obvious which modules your code depends on
4. **IDE/Editor Issues**: Auto-completion and static analysis tools struggle
5. **Maintenance Nightmare**: Difficult to track down bugs and understand code flow

**Better Alternatives:**

```python
# GOOD: Explicit imports
import math
import statistics

print(math.sin(1))
print(statistics.mean([1, 2, 3]))

# GOOD: Selective imports
from math import sin, cos, pi
from statistics import mean, median

print(sin(1))
print(mean([1, 2, 3]))

# GOOD: Aliased imports for long module names
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([1, 2, 3])
plt.plot(arr)
```

**When Wildcard Imports Might Be Acceptable:**
- In interactive Python sessions for convenience
- When importing from modules specifically designed for it (like `tkinter.constants`)
- In certain testing scenarios

**Example of Namespace Pollution Problem:**

```python
# pollution_example.py
from os import *
from sys import *

# Now you have dozens of names in your namespace!
# What if you accidentally name a variable 'path'?
path = "my_custom_path"  # This shadows os.path!

# Later in code:
# result = path.join("folder", "file")  # ERROR! 'str' has no 'join' method
```

**Best Practices:**
- Use explicit imports (`import module` or `from module import specific_function`)
- Use meaningful aliases for long module names
- Be explicit about what you're importing
- Keep imports at the top of the file for clarity

---

## 3. **Intermediate**: Function Name Conflicts

### Question:
Consider the following two module files, `helpers1.py` and `helpers2.py`, and a script `main.py`, all in the same directory.

`helpers1.py`:
```python
def get_data():
    return "Data from helpers1"
```

`helpers2.py`:
```python
def get_data():
    return "Data from helpers2"
```

`main.py`:
```python
from helpers1 import get_data
from helpers2 import get_data

print(get_data())
```

What will be printed to the console when `main.py` is executed, and why? How could you modify `main.py` to access the `get_data` function from both modules?

### Answer:

**Output:**
```
Data from helpers2
```

**Explanation:**
The second import (`from helpers2 import get_data`) overwrites the first import. In Python, when you import a function with the same name twice, the later import overwrites the earlier one in the current namespace. So `get_data` refers to the function from `helpers2` only.

**Solutions to Access Both Functions:**

**Solution 1: Use Module Import**
```python
# main.py
import helpers1
import helpers2

print(helpers1.get_data())  # Output: Data from helpers1
print(helpers2.get_data())  # Output: Data from helpers2
```

**Solution 2: Use Aliases with Selective Import**
```python
# main.py
from helpers1 import get_data as get_data1
from helpers2 import get_data as get_data2

print(get_data1())  # Output: Data from helpers1
print(get_data2())  # Output: Data from helpers2
```

**Solution 3: Use Module Aliases**
```python
# main.py
import helpers1 as h1
import helpers2 as h2

print(h1.get_data())  # Output: Data from helpers1
print(h2.get_data())  # Output: Data from helpers2
```

**Solution 4: Mixed Approach**
```python
# main.py
from helpers1 import get_data
import helpers2

print(get_data())           # Output: Data from helpers1
print(helpers2.get_data())  # Output: Data from helpers2
```

**Complete Example with File Structure:**

```python
# helpers1.py
def get_data():
    return "Data from helpers1"

def process_data():
    return "Processing in helpers1"

# helpers2.py
def get_data():
    return "Data from helpers2"

def process_data():
    return "Processing in helpers2"

# main.py - Demonstrating different approaches
import helpers1
import helpers2
from helpers1 import get_data as get_data1
from helpers2 import get_data as get_data2

print("=== Module Import Approach ===")
print(helpers1.get_data())
print(helpers2.get_data())

print("\n=== Alias Approach ===")
print(get_data1())
print(get_data2())

print("\n=== Accessing Other Functions ===")
print(helpers1.process_data())
print(helpers2.process_data())
```

**Key Lessons:**
- Function names imported directly into the namespace can conflict
- Later imports overwrite earlier ones with the same name
- Use explicit module references or aliases to avoid conflicts
- This is another reason why wildcard imports (`from module import *`) are discouraged

---

## 4. **Advanced**: Script vs Module Execution

### Question:
In Python, a file can be used as either a script to be run directly or as a module to be imported. How can you write code within a file that executes only when the file is run as a script, but not when it is imported as a module? Provide a code example.

### Answer:

Use the `if __name__ == "__main__":` idiom. This checks whether the module is being run directly as a script or being imported.

**How It Works:**
- When a Python file is run directly, Python sets `__name__` to `"__main__"`
- When a Python file is imported as a module, Python sets `__name__` to the module's name

**Basic Example:**

```python
# utility_module.py
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers and return the result."""
    return a * b

def main():
    """Main function to run when script is executed directly."""
    print("Running ut