class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.ans = []

    def pre_order(self):
        node = self.root

        def walk(node):
            self.ans.append(node.value)
            if node.left:
                walk(node.left)
            if node.right:
                walk(node.right)

        walk(node)
        return self.ans



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

def tree_intersection(tree1, tree2):
    value_bank = HashTable()
    answers = []
    inorder(value_bank, tree1, answers)
    inorder(value_bank, tree2, answers)
    return answers


def inorder(hashmap, tree, list):
    def walk(root):
        if root is None:
            return
        walk(root.left)
        if hashmap.contains(str(root.value)):
            list.append(root.value)
        else: 
            hashmap.set(str(root.value), None)
        walk(root.right)

    walk(tree.root)