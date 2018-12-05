class Node:
    def __init__(self, dado):
        self.dado = dado
        self.next = Node

class Fila:

    def __init__(self):
        self.prim = None
        self.ulti = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.ulti is None:
            self.ulti = node
        else:
            self.ulti.next = node
            self.ulti = node
        if self.prim is None:
            self.prim = node

        self._size = self._size + 1


    def pop(self):
        if self._size > 0:
            elem = self.prim.dado
            self.prim = self.prim.next
            self._size = self._size - 1
            return elem
        raise IndexError("A fila não tem ninguém")

    def peek(self):
        if self._size > 0:
            elem = self.prim.dado
            return elem
        raise IndexError("A fila não tem ninguém")


    def __len__(self):
        return self._size


    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.prim
            while(pointer):
                r = r + str(pointer.dado) + "->"
                pointer = pointer.next
            return r
        return "Fila vazia"


    def __str__(self):
        return self.__repr__()
