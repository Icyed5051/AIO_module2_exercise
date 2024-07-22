import numpy as np

# Define a square matrix A (e.g., 3x3)
A = np.array([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
])


def inverse_matrix ( matrix ):
    # Check if the matrix is invertible by checking its determinant
    det = np.linalg.det(A)
    if det == 0:
        print("Matrix is not invertible.")
    else:
        # Compute the inverse of the matrix A
        A_inv = np.linalg.inv(A)
    return A_inv


print(inverse_matrix(A))
