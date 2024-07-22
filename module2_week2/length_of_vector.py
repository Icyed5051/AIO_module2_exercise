import numpy as np
import math


def compute_vector_length(vector):
    result = 0
    for i in range(len(vector)):
        result += pow(vector[i], 2)
    return result


vector = np.array([1, 2, 3, 4, 5])
print(compute_vector_length(vector))
