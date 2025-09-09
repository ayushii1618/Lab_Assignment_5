import numpy as np
from scipy import linalg

# Define matrix
matrix = np.array([[4, 5],
                   [3, 2]])

# Determinant
det = linalg.det(matrix)

print("Matrix:\n", matrix)
print("Determinant:", det)
