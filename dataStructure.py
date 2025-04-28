# list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
grades = [x for x in range(100) if x % 3 == 1]
grades.sort()
grades.reverse()
grades.append(100)
grades.pop()
grades.remove(4)
print(grades)

import array as arr

numbers = arr.array('i', [1, 2, 3, 4])
print(numbers)  # خروجی: array('i', [1, 2, 3, 4])

from queue import Queue

q = Queue()
for i in range(23, 100):
    q.put(i)

print(q.get())

stack = []
stack.append(1)
stack.append(2)
print(stack.pop())


# no library
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)


# استفاده از پشته
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # خروجی: 2


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node}: {', '.join(map(str, self.graph[node]))}")


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.display()


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, value):
        self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def inorder(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.value, end=" ")
            self._inorder_traversal(node.right)


# استفاده از درخت
bt = BinaryTree(10)
bt.insert(5)
bt.insert(15)
bt.inorder()  # خروجی: 5 10 15


class DFS_recursive(Graph):
    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)


# استفاده از گراف و DFS
g = DFS_recursive()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS (Recursive):")
g.dfs_recursive(2)  # شروع از گره 2



class GraphWithDFS(Graph):
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                stack.extend(reversed(self.graph.get(vertex, [])))  # اضافه کردن همسایه‌ها به پشته

# استفاده از گراف و DFS
g = GraphWithDFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("\nDFS (Iterative):")
g.dfs_iterative(2)  # شروع از گره 2


class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def display(self):
        for node in self.graph:
            print(f"{node}: {', '.join(map(str, self.graph[node]))}")


class DirectedGraphWithDFS(DirectedGraph):
    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

# استفاده از گراف جهت‌دار و DFS
g = DirectedGraphWithDFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("DFS (Recursive) on Directed Graph:")
g.dfs_recursive(0)  # شروع از گره 0



class DirectedGraphWithDFS(DirectedGraph):
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                stack.extend(reversed(self.graph.get(vertex, [])))  # اضافه کردن همسایه‌ها به پشته

# استفاده از گراف جهت‌دار و DFS
g = DirectedGraphWithDFS()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("\nDFS (Iterative) on Directed Graph:")
g.dfs_iterative(0)  # شروع از گره 0

class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def has_cycle_util(self, v, visited, recursion_stack):
        visited.add(v)
        recursion_stack.add(v)

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                if self.has_cycle_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True

        recursion_stack.remove(v)
        return False

    def has_cycle(self):
        visited = set()
        recursion_stack = set()

        for node in self.graph:
            if node not in visited:
                if self.has_cycle_util(node, visited, recursion_stack):
                    return True
        return False

# استفاده از گراف جهت‌دار و تشخیص چرخه
g = DirectedGraph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # چرخه در اینجا

print("Graph has cycle:", g.has_cycle())  # خروجی: True



class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # چون گراف بدون جهت است

    def has_cycle_util(self, v, visited, parent):
        visited.add(v)

        for neighbor in self.graph.get(v, []):
            if neighbor not in visited:
                if self.has_cycle_util(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True

        return False

    def has_cycle(self):
        visited = set()

        for node in self.graph:
            if node not in visited:
                if self.has_cycle_util(node, visited, None):
                    return True
        return False

# استفاده از گراف بدون جهت و تشخیص چرخه
g = UndirectedGraph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)  # چرخه در اینجا

print("Graph has cycle:", g.has_cycle())  # خروجی: True



