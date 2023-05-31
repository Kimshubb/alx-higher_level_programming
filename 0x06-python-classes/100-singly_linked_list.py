#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data

    @property
    def data(self):
        ''' retrieve data'''
        return self.__data

    @data.setter
    def data(self, value):
        if value not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.head
        nodes = []
        while current:
            nodes.append(str(current.data))
            current = current.next
        return "\n".join(nodes)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

linkedlist1 = SinglyLinkedList()
linkedlist.sorted_insert(5)
linkedlist.sorted_insert(6)
linkedlist.sorted_insert(8)
