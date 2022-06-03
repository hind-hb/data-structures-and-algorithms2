from typing import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self,value):
        node=Node(value)
        if self.is_empty():
            self.front=node
            self.rear=node
        self.rear.next=node
        self.rear=node
    def dequeue(self):
        if self.is_empty():
            raise Exception("empty equeue")
        if self.front==self.rear:
            temp=self.front
            self.front=None
            self.rear=None
            return temp.value
        else:
            temp=self.front
            self.front=self.front.next
            temp.next=None
            return temp.value

    def peek(self):
       if self.is_empty():
           raise Exception("empty equeue")
       return self.front.value


    def is_empty(self):
     return not self.front

    def __len__(self):
        counter=0
        while self.front:
            counter +=1
            self.dequeue()
        return counter


class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self, root):
        # print(root.value)
        arr = []
        def walk(node):
            arr.append(node.value)
            if node.left != None:
                walk(node.left)

            if node.right != None:
                walk(node.right)

        walk(root)      
        return arr
        

    def post_order(self, root):
        try:
            if root.left:
                self.post_order(root.left)

            if root.right:
                self.post_order(root.right)

            self.arr.append(root.value)
            return self.arr
        except:
            raise Exception("something went wrong")

    def in_order(self, root):
    
        try:
            if root.left:
                self.in_order(root.left)

            self.arr.append(root.value)

            if root.right:
                self.in_order(root.right)

            return self.arr
        except:
            raise Exception("something went wrong")

    def test(self):
        self.arr = []

    def tree_max(self):

        x=self.in_order(self.root)
        self.max=0

        for i in x :
            if i>self.max:
                self.max=i
        return self.max
    
    
    def breadthFirst(self,root):
        
        if not root:
                raise Exception("Empty Tree")

        Queue_breadth = Queue()
        Queue_breadth.enqueue(root)

        try:
            while Queue_breadth.peek():
                
                    node_front = Queue_breadth.dequeue()
                    
                    self.arr.append(node_front.value)

                    if node_front.left:
                        Queue_breadth.enqueue(node_front.left)

                    if node_front.right:
                        Queue_breadth.enqueue(node_front.right)
            
        except:
            return self.arr



class BinarySearch(BinaryTree):

    def add(self, value):

        if not self.root:
            self.root = Node(value)
            # print(self.root.value)
            return

        current = self.root

        while current:
            if value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)

                    return

            else:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return

    def Contains(self, value):

        if not self.root:
            raise Exception("empty is tree")
        elif value == self.root.value:
            return True
        else:
            current = self.root
            while current:

                if current.value < value:

                    if current.right:
                        current = current.right
                        if value == current.value:
                            return True
                    else:
                        return False

                else:

                    if current.left:
                        current = current.left
                        if value == current.value:
                            return True
                    else:
                        return False



# x=Node(5)
# x.left=Node(68)
# x.right=Node(78)
# x.left.left=Node(8)
# x.right.right=Node(9)
# y=BinaryTree()
# y.root=x

# print(y.breadthFirst(x))