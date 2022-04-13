
from pyparsing import empty


class Node():
    # Define Node
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return str(self.value)

class Queue:
    # define functions of queue include enqueue for add value  , dequeue  for pop value and check is empty 
    def __init__(self):
        self.front = None
        self.rear = None
    
    def __str__(self):
        current = self.front
        items = []
        while current:
            items.append(str(current.value))
            current = current.next
        return " ".join(items)
    
    def enqueue(self, value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
    
    def dequeue(self):
        if not self.is_empty():
            empty = self.front
            self.front = self.front.next
            empty.next = None
            return empty.value
        
    def is_empty(self):
        if self.front:
            return False
        return True

class BinaryTrempty:
      
    def __init__(self):
        self.root=None


    def PreOrder(self):
        """
        Pre-order: root >> left >> right
        """    
        output_pre=[]
        def _walk(node):
            output_pre.append(node.value)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output_pre
    
    def InOrder(self):
        """
        In-order: left >> root >> right
        """        
        output_in=[]
        def _walk(node):
            if node.left:
                _walk(node.left)
            output_in.append(node.value)
            if node.right:
                _walk(node.right)
        _walk(self.root)
        return output_in

    def PostOrder(self):
        """
        Post-order: left >> right >> root
        """        
        output_post=[]
        def _walk(node):
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            output_post.append(node.value)
        _walk(self.root)
        return output_post

    def breadth_first(self):
        # Traverse the input trempty using a Breadth-first approach
            output = []
            empty = None
            queue = Queue()
            queue.enqueue(self.root)
            while queue.front:
                empty = queue.dequeue()
                output.append(empty.value)
                if empty.left:
                    queue.enqueue(empty.left)
                if empty.right:
                    queue.enqueue(empty.right)
            return output





