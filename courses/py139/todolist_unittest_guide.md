# TodoList unittest Practice Problems

## todolist.py

```python
class Todo:
    DONE_MARKER = "X"
    UNDONE_MARKER = " "

    def __init__(self, title):
        self.title = title
        self.done = False

    def __str__(self):
        return f"[{self.DONE_MARKER if self.done else self.UNDONE_MARKER}] {self.title}"

    def mark_done(self):
        self.done = True

    def mark_undone(self):
        self.done = False

class TodoList:
    def __init__(self, title):
        self.title = title
        self._todos = []

    def __str__(self):
        output = [f"---- {self.title} ----"]
        output.extend(str(todo) for todo in self._todos)
        return "\n".join(output)

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
        self._todos.append(todo)

    def size(self):
        return len(self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos[:]

    def item_at(self, index):
        if not -self.size() <= index < self.size():
            raise IndexError
        return self._todos[index]

    def mark_done_at(self, index):
        self.item_at(index).mark_done()

    def mark_undone_at(self, index):
        self.item_at(index).mark_undone()

    def is_done(self):
        return all(todo.done for todo in self._todos)

    def pop(self):
        return self._todos.pop()

    def remove_at(self, index):
        if not -self.size() <= index < self.size():
            raise IndexError
        return self._todos.pop(index)

    def mark_all_done(self):
        for todo in self._todos:
            todo.mark_done()

    def mark_all_undone(self):
        for todo in self._todos:
            todo.mark_undone()
```

## test_todolist.py Template

```python
import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")
        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    # Your tests go here

if __name__ == "__main__":
    unittest.main()
```

## unittest Practice Problems

Add these tests to your `TestTodoList` class.

**Problem 1:** Write a test to check the `size` of the list.

**Problem 2:** Write a test for the `first` method.

**Problem 3:** Write a test for the `last` method.

**Problem 4:** Write a test for `to_list` that checks if it returns a new list that is a copy, not the original `_todos` list.

**Problem 5:** Write a test for `is_done` that verifies it returns `False` when not all todos are done.

**Problem 6:** Write a test for `is_done` that verifies it returns `True` after marking all todos as done.

**Problem 7:** Write a test for `item_at` that verifies it returns the correct todo item.

**Problem 8:** Write a test for `item_at` to confirm it raises an `IndexError` when given an invalid index.

**Problem 9:** Write a test for `mark_done_at` to verify it correctly marks a specific todo as done.

**Problem 10:** Write a test for `mark_done_at` to confirm it raises an `IndexError` for an invalid index.

**Problem 11:** Write a test for `mark_undone_at`.

**Problem 12:** Write a test for `pop` to verify it removes and returns the last item in the list.

**Problem 13:** Write a test for `remove_at` to verify it removes the item at the specified index.

**Problem 14:** Write a test for `remove_at` to confirm it raises an `IndexError`.

**Problem 15:** Write a test for the `__str__` method to verify the string representation of an undone list.

**Problem 16:** Write another test for the `__str__` method, but this time, test the output after one of the todos has been marked as done.

**Problem 17:** Write a test for `add` to ensure it raises a `TypeError` if you try to add something that isn't a `Todo` object.

---

This setup is similar to the one in the Write a Test Suite for TodoList assignment from PY130.