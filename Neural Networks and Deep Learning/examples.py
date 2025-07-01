import numpy as np

# Example input arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Non-vectorized (loop-based)
result = []
for i in range(len(a)):
    result.append(a[i] + b[i])
print(result)
print("---")
# Vectorized (NumPy-based)
result = a + b

# Example 2: Element-wise multiplication
# Non-vectorized
result_mul = []
for i in range(len(a)):
    result_mul.append(a[i] * b[i])
print(result_mul)

print("---")
# Vectorized
result_mul = a * b

# Example 3: Dot product
# Non-vectorized
dot_product = 0
for i in range(len(a)):
    dot_product += a[i] * b[i]

print(dot_product)
print("---")

# Vectorized
dot_product = np.dot(a, b)

print(dot_product)
print("---")

# Example 4: Sum of all elements
c = np.array([[1, 2, 3], [4, 5, 6]])
# Non-vectorized
total_sum = 0
for row in c:
    for x in row:
        total_sum += x

# Vectorized
total_sum = np.sum(c)

# Example 5: Mean of elements along an axis
# Non-vectorized (mean of columns)
mean_cols = []
for j in range(c.shape[1]):
    col_sum = 0
    for i in range(c.shape[0]):
        col_sum += c[i, j]
    mean_cols.append(col_sum / c.shape[0])

# Vectorized (mean of columns)
mean_cols = np.mean(c, axis=0)
