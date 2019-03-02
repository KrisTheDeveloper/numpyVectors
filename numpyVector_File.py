import numpy as np

# by only putting in a single number it creates a (1,5) row vector vector
# Don't use this single number initialization
a = np.random.randn(5)
print(a)
print(a.shape)
print(a.T)

print(np.dot(a, a.T))

# this creates a (5,1) column vector
a = np.random.randn(5, 1)
print(a)
print(a.T)

# this should be added to github please
