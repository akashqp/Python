# Input: (Apple)(Ball)(Water)(Break)
# Output: Apple Ball Water Break
# Use Stack

def remove_brackets(s):
    stack = []
    result = ""
    for char in s:
        if char == "(":
            stack.append(result)
            result = ""
        elif char == ")":
            result = stack.pop() + " " + result
        else:
            result += char
    return result

s = "(Apple)(Ball)(Water)(Break)"
print(remove_brackets(s))