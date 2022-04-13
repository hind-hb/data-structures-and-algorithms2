# Tree Breadth first
## PR Link : [PR](https://github.com/hind-hb/data-structures-and-algorithms2/pull/17/commits/1ee001311acb42a6e734e2931ee8d92c35255f37)
##  Challenge Summary
 Write a function called breadth first
Arguments: tree
Return: list of all values in the tree, in the order they were encountered

## Whiteboard Process
![Untitled (1)](https://user-images.githubusercontent.com/75991604/163278761-f3c1c0e2-0e62-48e9-9b8e-5cd3a98dceff.jpg)


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

 def breadth_first(self):
            output = []
            
            em = None
            queue = Queue()
            
            queue.enqueue(self.root)
            
            while queue.front:
            
                em = queue.dequeue()
                
                output.append(em.value)
                
                if em.left:
                
                    queue.enqueue(em.left)
                    
                if em.right:
                
                    queue.enqueue(em.right)
                    
            return output
            
