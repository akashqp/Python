# Sum of diagonals of a matrix

class SumOfDiagonals:
    def sum_diagonal(self, matrix, m, n):
        sum = 0
        for i in range(0, m):
            for j in range(0, n):
                if i == j or i + j == m - 1:
                    print(matrix[i][j])
                    sum = sum + matrix[i][j]
        return sum
    
# Create object of the class
sum_diagonal = SumOfDiagonals()

matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
m = 3
n = 3

# Call the method to find sum of diagonals
print("Sum of diagonals is", sum_diagonal.sum_diagonal(matrix, m, n))