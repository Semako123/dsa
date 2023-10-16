from node import Node


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def push_front(self, val):
        new_node = Node(val)
        if self._head:
            new_node._next = self._head
            self._head = new_node
        else:
            self._head = new_node
            self._tail = new_node
        self._len += 1

    def pop_front(self):
        if self.empty():
            raise IndexError
        if self._head._next:
            value = self._head._value
            self._head = self._head._next
            self._len -= 1
        else:
            value = self._head._value
            self._head = None
            self._tail = None
            self._len -= 1
            return value

    def __str__(self):
        rep = ""
        current = self._head
        while current:
            rep += f"{current._value} -> "
            current = current._next
        return rep

    def push_back(self, val):
        new_node = Node(val)
        if self._tail:
            self._tail._next = new_node
            self._tail = new_node
        else:
            self._head = new_node
            self._tail = new_node
        self._len += 1

    def front(self):
        return self._head._value

    def back(self):
        return self._tail._value

    def insert(self, index, value):
        new_node = Node(value)
        if index > self._len - 1:
            raise IndexError
        elif index == 0:
            self.push_front(value)
        else:
            curr_node = self._head
            track = 1
            while curr_node:
                if track == index:
                    new_node._next = curr_node._next
                    curr_node._next = new_node
                    self._len += 1
                    return
                track += 1
                curr_node = curr_node._next

    def empty(self):
        return self._len == 0

    def size(self):
        return self._len
