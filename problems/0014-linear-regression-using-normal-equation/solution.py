import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)

	XT = np.transpose(X)
	A = np.linalg.inv(XT @ X)

	theta = A @ XT @ y

	return theta.tolist()

X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
