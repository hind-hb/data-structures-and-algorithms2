class MaxStack:

    def __init__(self):
        self.stack = []
        self.max = []

    def push(self, n):
        self.stack.append(n)
        if not self.max or n >= max(self.max):
            self.max.append(n)
    
    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val in self.max:
                self.max.remove(val)

    def top(self):
        if self.stack:
            return self.stack[-1]
    
    def peek_max(self):
        if self.maxes:
            return self.max[-1]
        
    def pop_max(self):
        if self.max:
            return self.max.pop()


if __name__ == '__main__':

    s = MaxStack()
    s.push(5)
    s.push(35)
    s.push(100)
    s.push(10)
    s.push(39)
    print(s.peek_max()) 


# class StackWithMax:
#     def __init__(self):
#         self.Stack = []
#         self.Max = []

#     def push(self, x):
#         self.Stack.append(x)
#         if (len(self.Stack) == 1):
#             self.Max.append(x)
#             return

#         # If current element is greater than
#         # the top element of track stack,
#         # append the current element to track
#         # stack otherwise append the element
#         # at top of track stack again into it.
#         if (x > self.Max[-1]):
#             self.Max.append(x)
#         else:
#             self.Max.append(self.Max[-1])

#     def getMax(self):
#         return self.Max[-1]

#     def pop(self):
#         self.Stack.pop()
#         self.Max.pop()


# # Driver Code
# if __name__ == '__main__':

#     s = StackWithMax()
#     s.push(20)
#     s.push(30)
#     s.push(75)
#     s.push(10)
#     s.push(50)
#     print(s.getMax()) 