import numpy as np
import math

def svd_2x2_singular_values(A):
    # Calculate A^T A
    B = A.T @ A

    a = B[0, 0]
    b = B[0, 1]
    d = B[1, 1]

    # Jacobi rotation angle
    theta = 0.5 * math.atan2(2 * b, a - d)

    c = math.cos(theta)
    s = math.sin(theta)

    # Rotation matrix
    V = np.array([
        [c, -s],
        [s,  c]
    ])

    # Diagonalize A^T A
    D = V.T @ B @ V

    # Eigenvalues
    eigenvalues = np.diag(D)

    # Singular values
    S = np.sqrt(np.maximum(eigenvalues, 0))

    # Sort descending
    order = np.argsort(S)[::-1]
    S = S[order]
    V = V[:, order]

    # Calculate U
    U = np.zeros((2, 2))

    for i in range(2):
        if S[i] > 1e-12:
            U[:, i] = (A @ V[:, i]) / S[i]

    # V transpose
    Vt = V.T

    return U, S, Vt