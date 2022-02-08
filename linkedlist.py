from node import Node,DNode
from pointers import *

class LinkedList:
    def __init__(self):
        self.front = NULLPTR
        self.length = 0

    def insert(self,index,entry):
        if index < 0 or index > self.length: raise Exception("Bad index!")
        temp = new(Node(entry))
        if index == 0:
            deref(temp).setNext(self.front)
            self.front = temp
        else:
            temp2 = self.front
            for _ in range(index - 1): temp2 = deref(temp2).getNext()
            deref(temp).setNext(deref(temp2).getNext())
            deref(temp2).setNext(temp)
        self.length += 1

    # remove the node at the index. If the index is invalid, raise Exception
    def remove(self,index:int): pass

    # return the entry from the node at the index
    def getEntry(self,index:int):
        if index < 0 or index > self.length: raise Exception("Bad index!")
        if self.length == 0: raise Exception("List is empty!")
        temp = self.front
        for _ in range(index): temp = deref(temp).getNext()
        return deref(temp).getEntry()

    # set the entry in the node at the index
    def setEntry(self,index:int,entry): pass

    # deletes all nodes
    def clear(self): pass

    # returns true if there is a node containing the entry, false otherwise
    def contains(self,entry) -> bool: pass

    def getLength(self) -> int:
        return self.length
    
    # returns a pointer to a deep copy
    def clone(self):
        copy = new(LinkedList())
        temp = self.front
        while temp != NULLPTR:
            deref(copy).insert(deref(copy).length,deref(temp).entry)
            temp = deref(temp).getNext()
        return copy
        
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

listt = new(LinkedList())
deref(listt).insert(0,4)
deref(listt).insert(1,5)
deref(listt).insert(1,3)
printObj(listt)