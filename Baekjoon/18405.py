import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
virus_num = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 좌표
            virus_num.append([graph[i][j], 0, i, j])

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus_num.sort()
q = deque(virus_num)
while q:
    num, sec, i, j = q.popleft()
    if sec == s:
        break
    for h in range(4):
        nx, ny = i+dx[h], j+dy[h]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = num
            q.append([num, sec+1, nx, ny])

print(graph[x-1][y-1])