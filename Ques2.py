from scipy import special

nums = [27, 64, 891]

# Cube root = pow(x, 1/3)
cube_roots = [special.cbrt(x) for x in nums]

print("Cubic Roots:", cube_roots)
