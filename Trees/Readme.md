# Tree Max Value
## PR Link : [PR](https://github.com/hind-hb/data-structures-and-algorithms2/pull/16/commits/2c9ad23c28d3b9ea43a97f3b0fd57103f55494f5)
##  Challenge Summary
Write the following method for the Binary Tree class

find maximum value

Arguments: none

Returns: number

## Whiteboard Process
![code-challange-166](https://user-images.githubusercontent.com/75991604/163284278-2cfa3115-fce0-4f96-b83c-d8e273176447.png)



## Approach & Efficiency
define function  find_Max_Value for the class Binarytree taken no arguments and return max value 

check if root is none return zero 

define insted function MAx_value taken root argument

check if the value in root more than max value 

max value equal root value 

check if the value in root left  max value in root left

check if the value in root right  max value in root right

return max Value 





## Solution

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
