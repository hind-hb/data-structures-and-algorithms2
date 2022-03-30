
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
        
            cur = self.head
            while cur:
                if cur.value == value:
                    return True
                cur = cur.next
            
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
            
            output+= "None"
        return output


    """append value"""
    def append(self, value):
        if self.head is None:
            self.head = value

        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = value
            
        """add value immediately before the first node that has the value specified"""
    def insert_before(self, value, newValue):
        if self.includes(value):
            cur = self.head
            prev= None
            while cur:
                if cur.value == value:
                    node = Node(newValue)
                    node.next = cur
                    if prev:
                        prev.next = node
                    else:
                        self.head = node
                    return self.__str__()
                prev = cur
                cur = cur.next
        else:
            return 'Value is not in the list'

        """ Adds a new value  after the Node specified """
    def insert_after(self, value, newValue):
        if self.includes(value):
            cur = self.head
            while cur:
                if cur.value == value:
                    node = Node(newValue)
                    node.next = cur.next
                    cur.next = node
                    return self.__str__()
                cur = cur.next
        else:
            return 'Value is not in the list'
    
        """
        This method  takes a number, k, as a parameter.
        Return the node’s value that is k from the end of the linked lis
        """
    def kthFromEnd(self, k):
        current = self.head

        length = 0
        while current is not None:
            current = current.next
            length += 1

        if k > length:
            return "Error - input value is greater than the length of the Linked List"
        elif k < 0:
            return "Error - input value is less than 0"

        current = self.head
        for i in range(1, (length - k)):
            current = current.next
        return current

        
        """zip two list in one list """
    def zip_list(self,list1,list2):
        # ll = LinkedList()
        # list1_current = list1.head
        # list2_current = list2.head
        # while list1_current != None or list2_current != None :
        #     if list1_current != None or list2_current != None :
        #         ll.insert(list1_current.value)
        #         ll.insert(list2_current.value)
        #         list1_current = list1_current.next
        #         list2_current = list2_current.next
        #     elif list1_current == None :
        #         ll.insert(list2_current.value)
        #         list2_current = list2_current.next
        #     elif list2_current == None :
        #         ll.insert(list1_current.value)
        #         list1_current = list1_current.next

        # return ll
     def zipLists(self,a,b):
          cur1, cur2 = a.head, b.head
          while cur1 and cur2:
           save1 = cur1.next
           save2 = cur2.next

           cur1.next = cur2
           cur2.next = save1

           cur1 = save1
           cur2 = save2

          return a



           


if __name__ == "__main__":


     ll =LinkedList()
     ll.insert(5)
     ll.insert(7)
     ll.insert(9)
     ll.append(5)
    #  ll.kthFromEnd(9)
    #  print(ll)

