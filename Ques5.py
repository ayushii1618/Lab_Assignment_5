import numpy as np
from scipy import linalg

# Define 2x2 array
matrix = np.array([[5, 4],
                   [6, 3]])

# Eigenvalues & Eigenvectors
eigenvalues, eigenvectors = linalg.eig(matrix)

print("Matrix:\n", matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
