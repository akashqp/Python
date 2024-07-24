# Program to check whether a number is a perfect number or not using concept of classes and objects

class PerfectNumber:
    def check_perfect_number(self, num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum = sum + i
        if sum == num:
            return True
        else:
            return False
        
# Create object of the class
perfect = PerfectNumber()

# Input number from user
num = int(input("Enter a number: "))

# Check whether the number is perfect number or not
if perfect.check_perfect_number(num):
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

