"""A tiny todo-list app (in-memory)."""


class TodoList:
    def __init__(self):
        self._items = []

    def add(self, title):
        if not title or not title.strip():
            raise ValueError("title must not be empty")
        self._items.append({"title": title.strip(), "done": False})
        return len(self._items) - 1

    def complete(self, index):
        self._items[index]["done"] = True

    def pending(self):
        return [i["title"] for i in self._items if not i["done"]]


if __name__ == "__main__":
    todos = TodoList()
    todos.add("write code")
    todos.add("push to git")
    todos.complete(0)
    print("Pending:", todos.pending())
