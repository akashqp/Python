class Frequency:
    def count_frequency(self, data, target):
        frequency = 0
        for i in data:
            if i == target:
                frequency += 1
        return frequency
    
# Create object of the class
frequency = Frequency()

data = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]
target = 1

# Call the method to count frequency of target element
print("Frequency of", target, "is", frequency.count_frequency(data, target))