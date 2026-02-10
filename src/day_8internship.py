#topic1

import numpy as np

brr=np.array([1,2,3,])
brr2=np.array([10])

result=brr/brr2
print(result)

#topic2

a=np.array([1,2,3,4,5])
a.shape

b=np.array([[1,2],[3,4]])
b.shape

"reshape"
arr=np.arange(12)
print(arr)

reshaped=np.reshape(arr,(3,4))
print(reshaped)

#task1

import numpy as np

# Step 1: Create a 5x3 array of random integers between 50 and 100
scores = np.random.randint(50, 101, size=(5, 3))

# Step 2: Calculate column-wise mean (mean of each subject)
subject_means = scores.mean(axis=0)

# Step 3: Subtract the mean from the original scores using broadcasting
centered_scores = scores - subject_means

# Step 4: Print results
print("Original Scores (5 students x 3 subjects):")
print(scores)

print("\nSubject-wise Mean Scores:")
print(subject_means)

print("\nCentered Scores (after broadcasting):")
print(centered_scores)

#task2

import numpy as np

# Step 1: Create a 1D array with values 0 to 23
data = np.arange(24)

# Step 2: Reshape into (4, 3, 2)
reshaped_data = data.reshape(4, 3, 2)

# Step 3: Transpose to get shape (4, 2, 3)
# Swap axis 1 and 2
final_data = reshaped_data.transpose(0, 2, 1)

# Step 4: Output
print("Final Shape:", final_data.shape)
print("Final Array:")
print(final_data)
