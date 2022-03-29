class Node:
    """class of create node"""
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
class  PseudoQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def enqueue(self, value):
        """
        enqueue from queue 
        """
        self.stack1.push(value)

    def dequeue(self):
        """
        dequeue from queue
        """
        while self.stack1.peek():
            if self.stack1.top.next == None:
                return self.stack1.top.value

            else:
                temp = self.stack1.pop()
                self.stack2.push(temp)
                continue
    

