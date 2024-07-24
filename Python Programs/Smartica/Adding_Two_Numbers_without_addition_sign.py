# Adding Two Numbers without addition sign

class Add:
    def add(self, a, b):
        while b != 0:
            carry = a & b
            a = a ^ b
            b = carry << 1
        return a
    
# Create object of the class
addition = Add()

a = 5
b = 2

# Call the method to add two numbers
print("Sum of", a, "and", b, "is", addition.add(a, b))

