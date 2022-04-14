
# Trees
A tree is a data structure in which data objects are linked together in a hierarchical fashion via references. Each tree has a root node from which we can access all of the tree's elements. Each node in the tree has zero or more children, starting with the root node.

## PR Link : [link](https://github.com/hind-hb/data-structures-and-algorithms2/pull/18/commits/8cba58ae6155b92b5c61a8807954184946b6458d#diff-61841206cfd2fdf0f20210b2926c4e31bf81a50a1903e4ba91d7ee1a09173a6cR55-R56)
## Challenge


Create a Node class that includes properties for the node's value, left child node, and right child node. Tree of Binary

Make a Binary Tree class, and then implement it. For each of the depth first traversals: pre order, in order, and post order, define a method that returns an array of the values, arranged correctly.

Tree of Binary Searches Tree , Make a Binary Search Tree class, and then implement it. This class should be a subclass of the Binary Tree Class, and it should have the following extra methods:

Methode Add

Arguments: worth Nothing is returned. Creates a new node in the binary search tree with the value at the correct location.

 Methode Contains

Argument: worth Returns: boolean indicating whether the value appears at least once in the tree.

## Approach & Efficiency
Big (O):
Time --> O(n)
Space --> O(1)

## API
### Node
The value stored in the node, the left child node, and the right child node all have properties. 

### Binary Tree 
This is the parent class for binary trees, which offers three methods for sorting data.
Root >> left >> right >> pre-order
Left >> root >> right, in that order
After that, the order is left >> right >> root.
Input: Nothing is being done: Returns an array of the values, arranged correctly, after traversing a tree.

### Binary Search Tree 
A subclass of BinaryTree used to add values to the tree and search for them
Add:
    Arguments: value
    Return: nothing
    Adds a new node with that value in the correct location in the binary search tree.
contains:     
    Argument: value
    Returns: boolean indicating whether or not the value is in the tree at least once.
