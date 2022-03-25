


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """class for stack """
    def __init__(self):
        self.top = None

    def push(self, value):

        """ Create New Node """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """ remove value of stack"""
        if self.is_empty():
            raise Exception("Stack is empty")
        node = self.top 
        self.top = self.top.next
        return node.value

        return temp.value

    def peek(self):
         """refer to the top of a stack """
         if self.is_empty():
            raise Exception("Stack is empty")
         return self.top.value

    def is_empty(self):
          """to check if the stack is empty """
          if self.top == None:
            return True
          return False

class Queue :
    """class for stack """
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,value):
        """ Create New Node """
        node = Node(value)

        if not self.front :
            self.rear = node
            self.front = node 
         
        else :
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        """ remove value of queue"""
        if self.front == None:
            raise Exception(" is an Empty Queue")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek_queue(self):
        """refer to the front of a queue """
        if self.front == None:
            raise Exception(" is an Empty Queue")
        return self.front.value

    def isEmpty_queue(self):
        """to check if the queue is empty """
        if self.front == None:
            return True
        else:
            return False


