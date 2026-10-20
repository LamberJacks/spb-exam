with open('input.txt', 'r') as file:
    n = int(file.readline())
    a = [list(map(float, file.readline().split())) for _ in range(n)]

det = 1

for i in range(n):

    pivot = i
    for j in range(i + 1, n):
        if abs(a[j][i]) > abs(a[pivot][i]):
            pivot = j

    if abs(a[pivot][i]) < 1e-10:
        det = 0
        break

    if pivot != i:
        a[i], a[pivot] = a[pivot], a[i]
        det *= -1
    det *= a[i][i]

    for j in range(i + 1, n):
        factor = a[j][i] / a[i][i]
        for k in range(i + 1, n):
            a[j][k] -= factor * a[i][k]
        a[j][i] = 0

print(round(det))
