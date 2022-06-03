# Code Challenge 32

##  Tree Intersection
  * Find common values in 2 binary trees.
## PR :  [LINK](https://github.com/hind-hb/data-structures-and-algorithms2/pull/26/commits/b3dc7bcfdb66bc40845e046f212a0969f986126f)
  
## Challenge Summary
  * Write a function that accepts a lengthy string parameter.
  * Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.
  
## Whiteboard Process
![cc32](https://user-images.githubusercontent.com/75991604/171827662-76b5efe9-7ab4-493e-ab02-786f6a086de7.jpeg)
## Solution

```
def hash_map_tree_intersection(tree1,tree2):
    arr=[]
    # arr=tree1.in_order(tree1.root)
    print(tree1.root)
    arr1=tree2.in_order(tree2.root)
    # print(arr)
    hash=HashTable()
    print(tree1.root.value)
    def convert_tree_to_hash(root):

            if root.left:
                convert_tree_to_hash(root.left)

            hash.add(str(root.value),str(root.value))
            print("x")

            if root.right:
                convert_tree_to_hash(root.right)


    convert_tree_to_hash(tree1.root)

    for i in arr1:
        if hash.contains(str(i)):
            arr.append(i)
    return arr
```

## Approach & Efficiency
  * Time: O(n)
  * Space: O(1)
  
