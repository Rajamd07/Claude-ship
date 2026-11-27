import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import TodoList  # noqa: E402


class TodoListTest(unittest.TestCase):
    def test_add_and_pending(self):
        t = TodoList()
        t.add("a")
        t.add("b")
        self.assertEqual(t.pending(), ["a", "b"])

    def test_complete(self):
        t = TodoList()
        i = t.add("a")
        t.complete(i)
        self.assertEqual(t.pending(), [])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            TodoList().add("  ")


if __name__ == "__main__":
    unittest.main()
