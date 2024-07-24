# Sort the elements of a stack in ascending order

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return "$"
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
        return -1
    
def sort_stack(stack):
    temp_stack = Stack()
    while not stack.isEmpty():
        temp = stack.pop()
        print(temp)
        while not temp_stack.isEmpty() and temp_stack.top() > temp:
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
    return temp_stack

stack = Stack()
stack.push(30)
stack.push(-5)
stack.push(18)
stack.push(14)
stack.push(-3)

sorted_stack = sort_stack(stack)
print("Sorted stack is", sorted_stack.stack)