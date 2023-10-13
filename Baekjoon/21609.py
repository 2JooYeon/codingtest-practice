from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 크기가 가장 큰 블록 그룹을 찾는 함수
def find_biggest_group():
    result = []
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                # 그룹에 일반 블록이 적어도 하나 있어야 하므로, 그룹의 시작은 일반 블록으로 한다.
                if graph[i][j]<=0:
                    continue
                group = [[i, j]]
                num = graph[i][j]
                visited[i][j] = 1
                q = deque()
                q.append([i, j])
                temp_rainbow = 0
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        nx, ny = x+dx[d], y+dy[d]
                        if nx<0 or nx>=n or ny<0 or ny>=n: continue
                        # 색이 같은 블록이면 그룹에 추가
                        if not visited[nx][ny] and graph[nx][ny] == num:
                            visited[nx][ny] = 1
                            group.append([nx, ny])
                            q.append([nx, ny])
                        # 무지개 블록이면 다른 블록에도 속할 수 있으므로, 방문 처리는 하지 않는다.
                        if graph[nx][ny] == 0 and [nx, ny] not in group:
                            temp_rainbow += 1
                            group.append([nx, ny])
                            q.append([nx, ny])
                    if len(group) < 2:
                        continue
                    result.append([group, temp_rainbow, i, j])

    result.sort(key=lambda x:(-len(x[0]), -x[1], -x[2], -x[3]))
    if len(result) == 0: return []
    biggest_group = result[0][0]
    return biggest_group


# 중력을 적용하는 함수
def take_gravity():
    for j in range(n):
        end = n-1
        for i in range(n-2, -1, -1):
            # 검은색 블록은 그대로 유지하고, 바닥 -1
            if graph[i][j] == -1:
                end = i-1
            # 확인하는 칸이 빈칸이 아니면
            if graph[i][j] >= 0:
                data = graph[i][j]
                # 현재 칸을 빈칸으로 만들고
                graph[i][j] = -2
                # 바닥이 빈칸이면 바닥에 현재 값을 넣고, 바닥 -1
                if graph[end][j] == -2:
                    graph[end][j] = data
                    end -= 1
                # 바닥이 채워져있으면 바닥을 -1하고 현재 값 넣기
                else:
                    end -= 1
                    graph[end][j] = data


# 배열 반시계 방향 90도 회전 함수
def rotate90():
    global graph
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[i][j] = graph[j][n-i-1]
    graph = new_graph


answer = 0
while True:
    group = find_biggest_group()
    if len(group) == 0:
        break
    answer += len(group)**2
    for x, y in group:
        graph[x][y] = -2
    take_gravity()
    rotate90()
    take_gravity()

print(answer)