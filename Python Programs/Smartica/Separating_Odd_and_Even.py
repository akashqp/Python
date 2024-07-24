# Separating odd and even numbers from a list without using % operator and using classes and objects

class OddEven:
    def separate_odd_even(self, num):
        odd = []
        even = []
        for i in num:
            if i & 1:
                odd.append(i)
            else:
                even.append(i)
        return odd, even
    
# Create object of the class
oddeven = OddEven()

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Separate odd and even numbers from the list
odd, even = oddeven.separate_odd_even(l)

# Display the separated odd and even numbers
print("Odd numbers:", odd)
print("Even numbers:", even)




