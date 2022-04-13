# Tree Breadth first
## PR Link : 
##  Challenge Summary
 Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process
<!-- Embedded whiteboard image -->

## Approach & Efficiency
define function  breadth_first for the class Binarytree taken no arguments and return the values in list 
declare varable output equal list , empty equal none and queue eqaul class of queue 
determine queue of enqueue is  a root 
iteration loop for queue in front 
assgin empty varable to enqueu of queue
append value in list output 
then if the empty from left enqueue from left 
if the empty from right enqueue from right 
return list output 



## Solution
--def breadth_first(self):
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
            return output--