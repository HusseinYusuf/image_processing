import numpy as np

# Sample data
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

# Normalization
min_vals = np.min(data, axis=0)
max_vals = np.max(data, axis=0)
normalized_data = (data - min_vals) / (max_vals - min_vals)

# Standardization
mean_vals = np.mean(data, axis=0)
std_devs = np.std(data, axis=0)
standardized_data = (data - mean_vals) / std_devs

print("Original Data:")
print(data)
print("\nNormalized Data:")
print(normalized_data)
print("\nStandardized Data:")
print(standardized_data)
