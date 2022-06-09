from Tree import BinaryTree , Node 
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    


class HashTable():
  def __init__(self ,size = 1024):
    """initialization hash table"""
    self.max = size 
    self.arr = [[] for i in range(self.max)] 
    

  def get_hash(self, key):
    """function to return the hash value using ASCII code"""
    h = 0
    for char in key:
        h += ord(char)
    hash_index= h % self.max 
    return hash_index
 
  def add(self ,key ,value):
    """Function the store key value pairs in the key index of list"""
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
          self.arr[h][idx] = (key,value)
          found = True
    if not found: # if not found store it 
      self.arr[h].append((key,value))

  def get(self, key):
    """function that return the value stored in the key index"""
    h = self.get_hash(key)
    for element in self.arr[h]:
      if element[0] == key:
        return element[1] # return the value

  def contains(self, key):
    h = self.get_hash(key)
    found = False
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0] == key:
        found = True
    return found

  def delete(self , key):
    """function that set the value of key to None"""
    h = self.get_hash(key)
    for idx , element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][idx]





def tree_intersection(binary_tree1,binary_tree2):
    """
    Write a function called tree intersection
    Arguments: two binary trees
    Return: array
    """
    array=[]
    hashtable=HashTable()
    

    if not  binary_tree1.root or not binary_tree2.root:
        return "one of the trees is empty"

    tree_arr1=binary_tree1.PreOrder()
    tree_arr2=binary_tree2.PreOrder()
    print(tree_arr1)
    print( tree_arr2)

    for test_sample in tree_arr1:
        hashtable.add(test_sample,test_sample)

    for element in tree_arr2:
        if hashtable.contains(element):
            array+=[element]
    
    if array==[]:
        return "input Trees there is not intersection"

    return array

if __name__=='__main__':
# tree 1
    binary_tree1=BinaryTree()
    binary_tree1.root=Node(150)
    binary_tree1.root.left=Node(100)
    binary_tree1.root.right=Node(250)
    binary_tree1.root.left.left=Node(75)
    binary_tree1.root.left.right=Node(160)
    binary_tree1.root.right.left=Node(200)
    binary_tree1.root.right.right=Node(350)
    binary_tree1.root.left.right.left=Node(125)
    binary_tree1.root.left.right.right=Node(175)
    binary_tree1.root.right.right.left=Node(300)
    binary_tree1.root.right.right.right=Node(500)
# tree 2
    binary_tree2=BinaryTree()
    binary_tree2.root=Node(42)
    binary_tree2.root.left=Node(100)
    binary_tree2.root.right=Node(600)
    binary_tree2.root.left.left=Node(15)
    binary_tree2.root.left.right=Node(160)
    binary_tree2.root.right.left=Node(200)
    binary_tree2.root.right.right=Node(350)
    binary_tree2.root.left.right.left=Node(125)
    binary_tree2.root.left.right.right=Node(175)
    binary_tree2.root.right.right.left=Node(4)
    binary_tree2.root.right.right.right=Node(500)

    print(tree_intersection(binary_tree1,binary_tree2))
    
    


    