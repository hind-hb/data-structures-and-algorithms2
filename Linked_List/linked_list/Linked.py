
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
"""class LinkedList """
class LinkedList:
    def __init__(self):
        self.head = None
    """insert value"""
    def insert(self,value):
       
         node = Node(value)
         if self.head:
          node.next = self.head
         self.head = node

    """check include value"""
    def includes(self, value):
        
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            
            return False
    
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while(current):
                output+= f'{current.value} -->'
                current = current.next
            
            output+= "Null"
        return output

if __name__ == "__main__":


     ll =LinkedList()

     ll.insert("C")
     ll.insert("B")
     ll.insert("A")
#print(ll)
# print(ll.includes("B"))
