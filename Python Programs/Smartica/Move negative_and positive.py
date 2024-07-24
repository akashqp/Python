# Move negative numbers to beginning and positive numbers to end, the array should also be sorted in ascending order
# Input: [-1, 2, -3, 4, 5, -6, -7, 8]
# Output: [-1, -3, -6, -7, 2, 4, 5, 8]

class NegativePositive:
    def move_negative_positive(self, num):
        l = 0
        for i in range(len(num)):
            if num[i] < 0:
                temp = num[i]
                # Remove the negative number from the list
                num.pop(i)
                # Insert the negative number at the beginning of the list
                num.insert(l, temp)
                l += 1

if __name__ == "__main__":
    negpos = NegativePositive()
    l = [-1, 2, -3, 4, 5, -6, -7, 8]
    negpos.move_negative_positive(l)
    print("Array after rearranging:", l)