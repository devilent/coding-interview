from data_structure.node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_first(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def add_last(self, data):
        node = Node(data)
        current = self.head
        if not current:
            self.head = node
            return

        while current.get_next():
            current = current.get_next()
        current.set_next(node)

    def pop(self) -> Node:
        if self.empty():
            return None
        temp = self.head
        self.head = self.head.get_next()
        return temp

    def push(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def get_first(self) -> Node:
        return self.head

    def get_last(self) -> Node:
        current = self.head
        while current.get_next():
            current = current.get_next()
        return current

    def get(self, index) -> Node:
        count = 0
        current = self.head
        while current:
            if count == index:
                return current
            current = current.get_next()
            count += 1
        return None

    def empty(self) -> bool:
        if self.head:
            return False
        return True

    def delete(self, index):
        if index == 0:
            self.head = self.head.get_next()
        count = 0
        current = self.head.get_next()
        prev = None
        while current:
            if count == index:
                prev.set_next(current.get_next())
                return
            prev = current
            current = current.get_next()
            count += 1

    def __str__(self):
        if not self.head:
            return "None"
        current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count 