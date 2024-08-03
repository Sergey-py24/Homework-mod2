def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        matrix.append(a)
        for j in range(m):
            a.append(value)

    print(matrix)


result1 = get_matrix(3, 3, 33)
result2 = get_matrix(4, 4, 44)
result3 = get_matrix(5, 5, 55)
