import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Multiplication:", a * b)
print("Square:", a ** 2)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
C = np.matmul(A, B)

print("Matrix Product:\n", C)

data = np.array([10, 20, 30, 40, 50])

# Get values greater than 25
filtered = data[data > 25]

print(filtered)

scores = np.array([70, 80, 90, 60, 85])

print("Mean:", np.mean(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))
print("Standard Deviation:", np.std(scores))

arr = np.arange(1, 13)

matrix = arr.reshape(3, 4)

print(matrix)

# Random integers
rand_ints = np.random.randint(1, 100, size=(3, 3))

# Normal distribution
rand_norm = np.random.randn(2, 2)

print(rand_ints)
print(rand_norm)

A = np.array([[1, 2, 3],
              [4, 5, 6]])

B = np.array([1, 1, 1])

print(A + B)

# Features (X)
X = np.array([[1, 2],
              [2, 3],
              [3, 4]])

# Weights
w = np.array([0.4, 0.6])

# Prediction
y_pred = np.dot(X, w)

print(y_pred)

# Python loop
result = []
for i in range(5):
    result.append(i * 2)

print(result)

# NumPy version
arr = np.arange(5)
print(arr * 2)

a = np.array([5, 10, 15, 20])

# Replace values > 10 with 0
a[a > 10] = 0

print(a)

a = np.array([1, 2])
b = np.array([3, 4])

combined = np.concatenate((a, b))

print(combined)

grades = np.array([[80, 75, 90],
                   [60, 65, 70],
                   [85, 88, 92]])

# Average per student
avg_per_student = np.mean(grades, axis=1)

# Best subject scores
best_subject = np.max(grades, axis=0)

print("Average per student:", avg_per_student)
print("Best per subject:", best_subject)

image = np.array([[255, 0, 0],
                  [0, 255, 0],
                  [0, 0, 255]])

# Normalize pixel values
normalized = image / 255.0

print(normalized)
