# Find the next greater number with same set of digits
# Input 1: 3
# Input 2: 182
# Output: 218

# Give comments on the code below


def next_greater_number(n):
    num = list(str(n))
    # find permutations of the number
    permutations = []
    for i in range(len(num)):
        for j in range(len(num)):
            if i != j:
                temp = num[i]
                num[i] = num[j]
                num[j] = temp
                permutations.append(int(''.join(num)))
    # sort the permutations
    permutations.sort()
    # print the next greater number
    for i in permutations:
        if i > n:
            return i
    return -1

# Input number from user
num = int(input("Enter a number: "))
result = next_greater_number(num)

# Check whether the next greater number is found or not
if result == -1:
    print("No greater number found")    
else:
    print("Next greater number is:", result)