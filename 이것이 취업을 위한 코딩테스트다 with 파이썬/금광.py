t = int(input())
answers = []
for _ in range(t):
    answer = 0
    n, m = map(int, input().split())
    gold = []
    data = list(map(int, input().split()))
    for i in range(0, n):
        start = i*m
        end = i*m + m
        gold.append(data[start:end])
    d = [[0 for _ in range(m)] for _ in range(n)]
    d[0][0], d[1][0], d[2][0] = gold[0][0], gold[1][0], gold[2][0]
    dxdy = [(-1, -1), (0, -1), (1, -1)]
    for y in range(m):
        for x in range(n):
            for dx, dy in dxdy:
                nx, ny = x+dx, y+dy
                if 0 <= nx < n and 0 <= ny < n:
                    d[x][y] = max(d[x][y], gold[x][y] + d[nx][ny])

    for i in range(n):
        answer = max(answer, d[i][m-1])
    answers.append(answer)

for answer in answers:
    print(answer)
