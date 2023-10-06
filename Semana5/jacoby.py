import numpy as np

def jacobi(A, b, x0, tol=1e-6, max_iter=100):
    """
    Solves the system of linear equations Ax = b using the Jacobi method.
    
    Parameters:
        A (numpy.ndarray): The coefficient matrix of the system.
        b (numpy.ndarray): The constant vector of the system.
        x0 (numpy.ndarray): The initial guess for the solution.
        tol (float): The tolerance for the residual norm.
        max_iter (int): The maximum number of iterations.
    
    Returns:
        x (numpy.ndarray): The solution vector.
        residuals (list): The residual norms at each iteration.
    """
    n = len(b)
    x = x0.copy()
    residuals = []
    for k in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            s = sum(A[i, j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i, i]
        r = np.linalg.norm(A @ x_new - b)
        residuals.append(r)
        if r < tol:
            break
        x = x_new
    return x, residuals

# Example usage
A = np.array([[4.0, 1.0, -1.0],
              [2.0, 3.0, 0.0],
              [1.0, -1.0, 4.0]])
b = np.array([1.0, 2.0, 4.0])

x0 = np.array([0, 0, 0])

x, residuals = jacobi(A, b, x0, tol=1e-8, max_iter=1000)
for i, r in enumerate(residuals):
    print(f"Iteration {i}: Residual = {r:.6f}")
print(f"Solution: {x}")
