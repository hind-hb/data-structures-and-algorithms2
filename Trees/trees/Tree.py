class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    

class BinaryTree:
      
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
        
    def max_value(self):
        if self.root == None:
          return 0
        maximum_value = self.root.value
        def maximum_value_fun(root):
          nonlocal maximum_value
          if root.value > maximum_value:
              maximum_value = root.value
          if root.left:
              maximum_value_fun(root.left)
          if root.right:
              maximum_value_fun(root.right)
          return maximum_value
        return maximum_value_fun(self.root)


class binarySearchTree(BinaryTree):
    '''Search in Tree'''
    def add(self,value):
           
        if not self.root:
            self.root=Node(value)
        else:
            def _walk(node):
                if value<node.value:
                    if not node.left:
                        node.left=Node(value)
                        return
                    else:
                        _walk(node.left)


                else:
                    if not node.right:
                        node.right=Node(value)
                        return

                    else:
                        _walk(node.right)
            _walk(self.root)
    
    