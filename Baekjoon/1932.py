n = int(input())
triangle = []
d = []
for i in range(n):
    triangle.append(list(map(int, input().split())))
    d.append([0] * (i+1))
d[0][0] = triangle[0][0]
for x in range(1, n):
    for y in range(x+1):
        # 왼쪽 대각선 위 (x-1, y-1)
        if x-1 >= 0 and 0 <= y-1 <= x-1:
            d[x][y] = max(d[x][y], triangle[x][y] + d[x-1][y-1])
        # 오른쪽 대각선 위 (x-1, y)
        if x-1 >= 0 and 0 <= y <= x-1:
            d[x][y] = max(d[x][y], triangle[x][y] + d[x - 1][y])
print(max(d[n-1]))