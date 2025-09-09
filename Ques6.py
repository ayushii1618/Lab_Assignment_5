import numpy as np
from scipy import sparse

# Create Sparse Matrices
A = sparse.csr_matrix([[1, 0, 0], [0, 0, 2], [0, 3, 0]])
B = sparse.csc_matrix([[0, 5, 0], [0, 0, 0], [7, 0, 9]])

print("Sparse Matrix A (CSR):\n", A)
print("Sparse Matrix B (CSC):\n", B)

# Functions
print("\nA + B:\n", (A + B).toarray())
print("A Transpose:\n", A.transpose().toarray())
print("A * B:\n", (A @ B).toarray())
