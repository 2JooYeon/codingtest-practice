# from collections import deque
#
#
# def check_ice(graph, visited, x, y):
#     # 이미 방문했거나, 칸막이인 경우
#     if visited[x][y] or graph[x][y]:
#         return False
#     # 상하좌우
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     w, h = len(graph[0]), len(graph)
#     visited[x][y] = 1
#     q = deque([[x, y]])
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                 continue
#             if not visited[nx][ny] and not graph[nx][ny]:
#                 visited[nx][ny] = 1
#                 q.append([nx, ny])
#     return True
#
#
#
#
#
# answer = 0
# n, m = map(int, input().split())
# ice_tray = []
# visited = [[0 for _ in range(m)] for _ in range(n)]
#
# for _ in range(n):
#     ice_tray.append(list(map(int, list(input()))))
#
# for i in range(n):
#     for j in range(m):
#         if check_ice(ice_tray, visited, i, j):
#             answer += 1
#
# print(answer)


def check_ice(graph, visited, i, j):
    w, h = len(graph[0]), len(graph)
    if i < 0 or i >= h or j < 0 or j >= w:
        return False

    if visited[i][j] or graph[i][j]:
        return False

    visited[i][j] = 1
    check_ice(graph, visited, i-1, j)
    check_ice(graph, visited, i+1, j)
    check_ice(graph, visited, i, j-1)
    check_ice(graph, visited, i, j+1)
    return True


answer = 0
n, m = map(int, input().split())
ice_tray = []
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    ice_tray.append(list(map(int, list(input()))))

for i in range(n):
    for j in range(m):
        if check_ice(ice_tray, visited, i, j):
            answer += 1
print(answer)
