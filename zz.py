import numpy as np

def gaussJordan(a, b):
    n, _ = np.shape(a)
    A = np.c_[a, b]
    
    for i in range(n):
        for j in range(n):
            # Si el término ya es cero, continúa con el siguiente
            if (A[j, i] != 0 and A[i, i] != 0 and i != j):
                # factor de reducción
                f = A[j, i] / A[i, i]
                A[j, i + 1: n + 1] = A[j, i + 1: n + 1] - f * A[i, i + 1: n + 1]
        
        # Imprimir la matriz triangular en cada paso
        print(f'Paso {i + 1}:')
        print(A)
        print()

    # aplica la sustitución inversa
    x = np.zeros(n)
    for i in range(n):
        x[i] = A[i, n] / A[i, i]

    return x

def main():
    a = np.array([[55.8, 20.4, 17.1, 18.5, 19.2],
                  [7.8, 52.1, 12.3, 13.9, 18.5],
                  [16.4, 11.5, 46.1, 11.5, 21.3],
                  [11.7, 9.2, 14.1, 47.0, 10.4],
                  [8.3, 6.8, 10.4, 9.1, 30.6]])

    b = np.array([2500, 2000, 2500, 2000, 1000])
    n, c = np.shape(a)
    r = np.linalg.matrix_rank(a)
    ab = np.c_[a, b]
    ra = np.linalg.matrix_rank(ab)

    print('rango (A)={} rango (Ab) ={} n ={} '.format(r, ra, n))

    if (r == ra == n):
        print('solución única ')
        x = gaussJordan(a, b)
        print('Solución:')
        print(x)

    if (r == ra < n):
        print('múltiples soluciones ')

    if (r < ra):
        print('sin solución ')

if __name__ == "__main__":
    main()
