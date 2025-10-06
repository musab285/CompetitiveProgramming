def print_matrix(matrix):
    for row in matrix:
        print(["{0:8.4f}".format(value) for value in row])
    print()

def gauss_jordan_solve(coeff_matrix, constants):
    size = len(coeff_matrix)
    augmented = [coeff_matrix[i] + [constants[i]] for i in range(size)]
    for pivot_index in range(size):
        if augmented[pivot_index][pivot_index] == 0:
            for row_index in range(pivot_index + 1, size):
                if augmented[row_index][pivot_index] != 0:
                    augmented[pivot_index], augmented[row_index] = augmented[row_index], augmented[pivot_index]
                    break
        pivot_value = augmented[pivot_index][pivot_index]
        augmented[pivot_index] = [value / pivot_value for value in augmented[pivot_index]]
        for row_index in range(size):
            if row_index != pivot_index:
                factor = augmented[row_index][pivot_index]
                augmented[row_index] = [
                    augmented[row_index][col] - factor * augmented[pivot_index][col]
                    for col in range(size + 1)
                ]
    return [augmented[i][-1] for i in range(size)]

def invert_matrix(matrix):
    size = len(matrix)
    augmented = [matrix[i] + [1 if i == j else 0 for j in range(size)] for i in range(size)]
    for pivot_index in range(size):
        if augmented[pivot_index][pivot_index] == 0:
            for row_index in range(pivot_index + 1, size):
                if augmented[row_index][pivot_index] != 0:
                    augmented[pivot_index], augmented[row_index] = augmented[row_index], augmented[pivot_index]
                    break
        pivot_value = augmented[pivot_index][pivot_index]
        augmented[pivot_index] = [value / pivot_value for value in augmented[pivot_index]]
        for row_index in range(size):
            if row_index != pivot_index:
                factor = augmented[row_index][pivot_index]
                augmented[row_index] = [
                    augmented[row_index][col] - factor * augmented[pivot_index][col]
                    for col in range(2 * size)
                ]
    return [row[size:] for row in augmented]

def multiply_matrix_vector(matrix, vector):
    size = len(matrix)
    return [sum(matrix[i][j] * vector[j] for j in range(size)) for i in range(size)]

def main():
    coefficients = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
    ]
    constants = [8, -11, -3]

    print("System of equations: Ax = b")
    print("A =")
    print_matrix(coefficients)
    print("b =", constants)

    solution_gj = gauss_jordan_solve([row[:] for row in coefficients], constants[:])
    print("Solution using Gauss-Jordan Method:", solution_gj)

    inverse_matrix = invert_matrix([row[:] for row in coefficients])
    print("\nInverse of A:")
    print_matrix(inverse_matrix)

    solution_inv = multiply_matrix_vector(inverse_matrix, constants)
    print("Solution using Inversion Algorithm:", solution_inv)

main()
