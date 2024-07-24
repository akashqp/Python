# Maximum elements product without using inbuilt functions
# I/p : [1,2,3,4,5]
# O/p : 20

class MaximumProduct:
    def max_product(self, arr):
        max1 = max2 = 0
        for i in arr:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
        return max1 * max2
    
# Create object of the class
max_product = MaximumProduct()

arr = [1, 2, 3, 4, 5]

# Call the method to find maximum product of two elements
print("Maximum product of two elements is", max_product.max_product(arr))
    