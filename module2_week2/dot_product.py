import numpy as np


def compute_dot_product(vector1, vector2):
    result = 0
    if (len(vector1) != len(vector2)):
        return "wrong size input"
    for i in range(len(vector1)):
        result += vector1[i] * vector2[i]

    return result


vector1 = np.array([1, 2, 3])
vector2 = np.array([1, 2, 3, 4])
print(compute_dot_product(vector1, vector2))
