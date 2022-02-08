from pointers import *

class Node:
    def __init__(self,entry):
        self.entry = entry
        self.next = NULLPTR

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def setEntry(self,entry):
        self.entry = entry

    def getEntry(self):
        return self.entry

class DNode:
    def __init__(self,entry) -> None:
        self.entry = entry
        self.next = NULLPTR
        self.prev = NULLPTR
    
    def setEntry(self,entry):
        self.entry = entry

    def getEntry(self):
        return self.entry

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next

    def setPrev(self,prev):
        self.prev = prev

    def getPrev(self):
        return self.prev