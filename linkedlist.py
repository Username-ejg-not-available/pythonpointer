from node import Node,DNode
from pointers import *

class LinkedList:
    def __init__(self):
        self.front = NULLPTR
        self.length = 0

    def clone(): pass

    def insert(self,index,entry):
        if index < 0 or index > self.length: raise Exception("Bad index!")
        temp = new(Node(entry))
        if index == 0:
            deref(temp).setNext(self.front)
            self.front = temp
        elif index == self.length:
            temp2 = self.front
            for _ in range(self.length - 1): temp2 = deref(temp2).getNext()
            deref(temp2).setNext(temp)
        else:
            temp2 = self.front
            for _ in range(index - 1): temp2 = deref(temp2).getNext()
            deref(temp).setNext(deref(temp2).getNext())
            deref(temp2).setNext(temp)
        self.length += 1

    def remove(self): pass

    def getEntry(self): pass

    def setEntry(self): pass

    def clear(self): pass

    def contains(self) -> bool: pass

class DLinkedList:
    def __init__(self):
        self.front = NULLPTR
        self.back = NULLPTR
        self.length = 0

    def insert(self,index,entry):
        if index > self.length or index < 0: raise Exception("Index out of bounds")
        node = new(DNode(entry))
        if index == 0:
            if self.front == NULLPTR: self.front = self.back = node
            else:
                deref(self.front).setPrev(node)
                deref(node).setNext(self.front)
                self.front = node
        elif index == self.length:
            if self.back == NULLPTR:
                deref(self.front).setPrev(node)
                deref(node).setNext(self.front)
                self.front = self.back = node
            else:
                deref(self.back).setNext(node)
                deref(node).setPrev(self.back)
                self.back = node
        else:
            temp2 = self.front
            for _ in range(index - 1): temp2 = deref(temp2).getNext()
            deref(node).setNext(deref(temp2).getNext())
            deref(node).setPrev(temp2)
            deref(deref(temp2).getNext()).setPrev(node)
            deref(temp2).setNext(node)
        self.length += 1

listt = new(DLinkedList())
deref(listt).insert(0,4)
deref(listt).insert(1,3)
deref(listt).insert(0,5)
printObj(listt)

list2 = new(LinkedList())
deref(list2).insert(0,4)
deref(list2).insert(1,3)
deref(list2).insert(0,5)
printObj(list2)