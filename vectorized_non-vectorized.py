import numpy as np
import matplotlib.pyplot as plt
import time

# Create two large vectors
size = 10_000_000
a = np.random.rand(size)
b = np.random.rand(size)

# Non-vectorized approach using a loop
def non_vectorized_addition(a, b):
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return result

# Vectorized approach using NumPy
def vectorized_addition(a, b):
    return a + b

# Measure execution time
start_nv = time.time()
result_nv = non_vectorized_addition(a[:10000], b[:10000])  # Reduce size for practicality
end_nv = time.time()

start_v = time.time()
result_v = vectorized_addition(a, b)
end_v = time.time()

nv_time = end_nv - start_nv
v_time = end_v - start_v

# Plot comparison
plt.figure(figsize=(8, 4))
bars = plt.bar(['Non-Vectorized (loop, 10K)', 'Vectorized (NumPy, 10M)'], [nv_time, v_time])
bars[0].set_color('red')
bars[1].set_color('green')
plt.title('Execution Time Comparison')
plt.ylabel('Time (seconds)')
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()

nv_time, v_time
