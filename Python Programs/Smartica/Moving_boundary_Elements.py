# I/P = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# O/P = [ [4, 1, 2], [7, 5, 3], [8, 9, 6] ]

class MovingBoundaryElements:
    def move_boundary_elements(self, matrix, m, n):
        # Define a new empty matrix of m x n
        new_matrix = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    # Move boundary elements by one position
                    if i == 0 and j < n-1:
                        new_matrix[i][j+1] = matrix[i][j]
                    if j == n-1 and i < m-1:
                        new_matrix[i+1][j] = matrix[i][j]
                    if i == m-1 and j > 0:
                        new_matrix[i][j-1] = matrix[i][j]
                    if j == 0 and i > 0:
                        new_matrix[i-1][j] = matrix[i][j]
                else:
                    new_matrix[i][j] = matrix[i][j]

        return new_matrix
    
# Create object of the class
move_boundary = MovingBoundaryElements()

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
m = 3
n = 3

# Call the method to move boundary elements by one position
print("Matrix after moving boundary elements by one position is", move_boundary.move_boundary_elements(matrix, m, n))
