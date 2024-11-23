num_i = int(input()) + 1
num_j = int(input()) + 1
with open('data.txt', 'r') as f:
    a = f.read().splitlines()
matrix = []
for i in a:
    append_i = i.split()
    append_i = list(map(int, append_i))
    append_i.append(0)
    append_i.reverse()
    append_i.append(0)
    append_i.reverse()
    matrix.append(append_i)
matrix.append([0] * len(matrix[0]))
matrix.reverse()
matrix.append([0] * len(matrix[0]))
matrix.reverse()


summ = 0
for i in range(num_i - 1, num_i + 2):
    for j in range(num_j - 1, num_j + 2):
        summ += matrix[i][j]
summ -= matrix[num_i][num_j]
print(summ)