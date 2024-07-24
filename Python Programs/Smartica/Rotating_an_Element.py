# Rotating Array Elements
# I/p : [1,2,3,4,5]
# O/p : [5,1,2,3,4]

class RotateArray:
    def rotate_array(self, arr):
        last = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last
        return arr
    
# Create object of the class
rotate = RotateArray()

arr = [1, 2, 3, 4, 5]

# Call the method to rotate array elements
print("Rotated array is", rotate.rotate_array(arr))