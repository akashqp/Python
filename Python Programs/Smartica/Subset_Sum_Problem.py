#  Subset Sum Problem
# a = {1, 2, 1}
# Sum = 3
# Output = {[1, 2], [2, 1]}

class SubsetSum:
    def find_subset(self, data, target):
        result = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                if data[i] + data[j] == target:
                    result.append([data[i], data[j]])
        return result
    
# Create object of the class
subset_sum = SubsetSum()

data = [1, 2, 1]
target = 3

# Call the method to find subset of two elements whose sum is equal to target
print("Subset of two elements whose sum is equal to target is", subset_sum.find_subset(data, target))