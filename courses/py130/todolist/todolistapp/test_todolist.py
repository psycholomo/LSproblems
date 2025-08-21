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

    # your tests go here

    def test_length(self):
        self.assertEqual(3, len(self.todos))
    
    def test_to_list(self):
        # check to see if the function to_list returns a list
        self.assertEqual([self.todo1, self.todo2, self.todo3], self.todos.to_list())
    
    def test_first(self):
        self.assertEqual(self.todo1,self.todos.first())
    
    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())
    
    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
    
    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(1)
        
        with self.assertRaises(TypeError):
            self.todos.add("string")
    
    def test_todo_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0))
        with self.assertRaises(IndexError):
            self.todos.todo_at(5)
    
    def test_mark_done_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_done_at(6)
        
        self.todos.mark_done_at(1)
        self.assertFalse(self.todo1.done)
        self.assertTrue(self.todo2.done)
        self.assertFalse(self.todo3.done)
    
    def test_mark_undone_at(self):
        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(6)
        
        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo1.done)
        self.assertFalse(self.todo2.done)
        self.assertFalse(self.todo3.done)

    
    def test_mark_all_done(self):

        self.todos.mark_all_done()
        self.assertTrue(self.todo1.done)
        self.assertTrue(self.todo2.done)

    def test_remove_at(self):
        with self.assertRaises(IndexError):
            self.todos.remove_at(6)
        self.todos.remove_at(0)
        self.assertEqual([self.todo2, self.todo3], self.todos.to_list())
    
    def test_str(self):
        string = (
        "----- Today's Todos -----\n"
        "[ ] Buy milk\n"
        "[ ] Clean room\n"
        "[ ] Go to the gym"
        )
        self.assertEqual(string, str(self.todos))
    
    def test_each(self):
        results = []
        self.todos.each(lambda todo: results.append(todo))
        self.assertEqual([self.todo1, self.todo2,self.todo3], results)
    
    def test_select(self):
        
        self.todo1.done = True
        result = self.todos.select(lambda todo: todo.done)
        self.assertEqual(str(self.todo1), str(result))
if __name__ == "__main__":
    unittest.main()