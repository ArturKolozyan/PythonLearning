fn = input()
with open(fn, 'r') as f:
    a = f.read().splitlines()
matrix = []
for i in a:
    matrix.append(i.split())
t_matrix = []
t_matrix_string = []
k = -1
while k < len(matrix[0]) - 1:
    t_matrix_string = []
    k += 1
    for i in matrix:
        t_matrix_string.append(i[k])
    t_matrix.append(t_matrix_string)
print_matrix = []
for i in t_matrix:
    print_matrix.append(' '.join(i))
for i in print_matrix:
    print(i)
