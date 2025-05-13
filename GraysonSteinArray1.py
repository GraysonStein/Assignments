import numpy as np

# 1 - create array
array = np.random.randint(0, 5, (5, 5))

# 2 - print array
print("array:")
print(array)

# 3 - second row third column
print("Number at second row, third column:", array[1,2])

# 4 - sum
print("sum of al elements:", np.sum(array))

# 5 - mean
print("mean of each row:", np.mean(array, axis=1))

# 6 - maximum value
print("maximum value of each column:", np.max(array, axis=0))