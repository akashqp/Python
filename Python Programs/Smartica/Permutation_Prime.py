# Check whether the permutation of a number is prime or not

class Permutation:
    def check_prime(self, num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
    # Function to find permutation of a number
    def find_permutation(self, num):
        result = []
        num = list(str(num))  # Convert the number to a list of characters
        for i in range(len(num)):
            for j in range(len(num)):
                if i != j:
                    temp = num[i]
                    num[i] = num[j]
                    num[j] = temp
                    print(num)
                    if self.check_prime(int(''.join(num))):
                        result.append(int(''.join(num)))  # Convert the list back to a number
        return result

    
# Create object of the class
permutation = Permutation()

# Input number from user
num = int(input("Enter a number: "))
result = permutation.find_permutation(num)

# Check whether the permutation of the number is prime or not
if len(result) == 0:
    print("No permutation of the number is prime")
else:
    print("Permutation of the number is prime:", result)




# # Find permutations of a number
# def find_permutation(num):
#     result = []
#     num = list(str(num))  # Convert the number to a list of characters
#     for i in range(len(num)):
#         for j in range(len(num)):
#             if i != j:
#                 temp = num[i]
#                 num[i] = num[j]
#                 num[j] = temp
#                 result.append(int(''.join(num)))  # Convert the list back to a number
#     return result

# print(find_permutation(123))
