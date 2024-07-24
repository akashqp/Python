# Input: exp = "[()]{}{[()()]()}"
# Output: Balanced
# Input: exp = "[(])"
# Output: Not balanced

# Approach: Using Stack

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
    
def isBalanced(exp):
    stack = Stack()
    for char in exp:
        if char in ["(", "{", "["]:
            stack.push(char)
        else:
            if stack.isEmpty():
                return "Not balanced"
            top = stack.pop()
            if (char == ")" and top != "(") or (char == "}" and top != "{") or (char == "]" and top != "["):
                return "Not balanced"
    return "Balanced"

exp = "[()]{}{[()()]()}"
print(isBalanced(exp))

exp = "[(])"
print(isBalanced(exp))