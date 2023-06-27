import numpy as np

def exponential_decay(a, b, N):
    # a, b: exponential decay parameter
    # N: number of samples 
    return a * (1-b) ** np.arange(N)

print(exponential_decay(1, 0.10, 10))