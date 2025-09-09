import numpy as np
from scipy import linalg

# Same matrix as Task 3
matrix = np.array([[4, 5],
                   [3, 2]])

# Inverse
inv_matrix = linalg.inv(matrix)

print("Matrix:\n", matrix)
print("Inverse Matrix:\n", inv_matrix)
