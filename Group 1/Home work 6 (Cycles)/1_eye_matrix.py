"""
згенерувати квадратну матрицю 'око' - всі значення 0-лі а по діагоналі 1ки
"""

def eye_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
    return matrix

print(eye_matrix(3))
print(eye_matrix(4))

assert eye_matrix(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert eye_matrix(4) == [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

