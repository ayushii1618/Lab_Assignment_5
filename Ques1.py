import numpy as np
from scipy import io

# Create 4x4 array of ones
arr = np.ones((4, 4))

# Save to text file
np.savetxt("test.txt", arr)

# Load from text file
data = np.loadtxt("test.txt")

print("Original Array:\n", arr)
print("Loaded Data:\n", data)
