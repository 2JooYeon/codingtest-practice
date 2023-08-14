import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

answer = 999
n, m = map(int, input().split())
graph = []
# 빈칸의 좌표
blank = []
# 바이러스의 좌표
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 0:
            blank.append([i, j])
        if graph[i][j] == 2:
            virus.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(graph, visited, x, y):
    q = deque([[x, y]])
    visited[x][y] = 1
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = 1
                count += 1
    # 새롭게 퍼진 바이러스 개수 반환
    return count


wall_candi = combinations(blank, 3)
for wall in wall_candi:
    # 3개의 빈칸 조합 벽으로 변경
    for i, j in wall:
        graph[i][j] = 1
    # 방문 여부 초기화
    visited = [[0 for _ in range(m)] for _ in range(n)]
    # 퍼진 바이러스 개수 초기화
    virus_count = 0
    for i, j in virus:
        # 새롭게 퍼진 바이러스 개수 누적
        virus_count += bfs(graph, visited, i, j)
    answer = min(answer, virus_count)
    # 다시 빈칸으로 원상복구
    for i, j in wall:
        graph[i][j] = 0

# len(blank): 기존의 안전 영역 크기
# 3: 새롭게 추가한 벽의 개수
# answer: 새롭게 퍼진 바이러스의 개수
print(len(blank) - 3 - answer)