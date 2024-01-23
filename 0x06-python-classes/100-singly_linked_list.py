#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        newnode = Node(value)

        if not self.head:
            self.head = newnode
            return

        current = self.head
        while current.next_node:
            current = current.next_node

        current.next_node = newnode

    def __str__(self):
        result = []
        current = self.head

        while current:
            result.append(str(current.data))
            current = current.next_node
        result = sorted(result, key=lambda x: int(x))
        return '\n'.join(result)
