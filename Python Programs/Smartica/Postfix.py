# Input: A+B*C+D
# Output: ABC*+D+
# Input: ((A+B)-C*(D/E))+F
# Output: AB+CDE/*-F+

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
    
def infixToPostfix(exp):
    stack = Stack()
    result = ""
    for char in exp:
        if char.isalnum():
            result += char
        elif char in ["(", "{", "["]:
            stack.push(char)
        elif char in [")", "}", "]"]:
            while not stack.isEmpty() and stack.top() not in ["(", "{", "["]:
                result += stack.pop()
            stack.pop()
        else:
            while not stack.isEmpty() and stack.top() not in ["(", "{", "["] and precedence(char) <= precedence(stack.top()):
                result += stack.pop()
            stack.push(char)
    
    while not stack.isEmpty():
        result += stack.pop()
    return result

def precedence(char):
    if char in ["+", "-"]:
        return 1
    if char in ["*", "/"]:
        return 2
    return 0

exp = "A+B*C+D"
print(infixToPostfix(exp))

exp = "((A+B)-C*(D/E))+F"
print(infixToPostfix(exp))