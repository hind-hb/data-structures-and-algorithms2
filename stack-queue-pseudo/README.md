PR Link : [PR](https://github.com/hind-hb/data-structures-and-algorithms2/pull/13/commits/498abbc583590d63b1f345fae3b0f4d9d15ff679)

# Challenge Summary
<!-- Description of the challenge -->
Stack Queue Pseudo
Create a new class called pseudoQueue.

This PseudoQueue class will implement our standard queue interface (the two methods listed below),.

Methods:

enqueue.
dequeue.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![code-challange-11](https://user-images.githubusercontent.com/75991604/160939542-5cd5f626-5282-4110-b7bb-00b9779df129.png)


## Solution
<!-- Show how to run your code, and examples of it in action -->
```class Node:
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
        if self.stack2.is_empty():
          if self.stack1.is_empty():
            raise IndexError("Can't dequeue from empty ")
      
        while not self.stack1.is_empty():
            last_stack1_item = self.stack1.pop()
            self.stack2.push(last_stack1_item) 

        return self.stack2.pop()
    

if __name__ =="__main__":
    q = PseudoQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    print(q.dequeue()) 
    ```
    # Testing 
    ``` 
    from stack_queue_pseudo.stackQueuePesudo import Node , Stack , PseudoQueue


def test_push_stack ():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.top.value
  expected = 6
  assert actual == expected 

def test_pop_stack ():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.pop()
  expected = 6
  assert actual == expected 

def test_peek_stack():
  stack = Stack()
  stack.push(2)
  stack.push(4)
  stack.push(6)

  actual = stack.peek()
  expected = 6
  assert actual == expected 

def test_isEmpty():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected


def test_enqueue_dequeue():
    queue = PseudoQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(5)
    queue.enqueue(8)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 5
    ```
    
    
