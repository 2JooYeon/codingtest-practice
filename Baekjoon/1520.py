import heapq

def bfs():
    q = []
    # 더 높은 곳 부터 방문하기 위해 우선순위 큐 사용
    heapq.heappush(q, [-graph[0][0], 0, 0])
    # 방문 횟수를 저장할 2차원 리스트
    visited[0][0] = 1
    while q:
        h, x, y = heapq.heappop(q)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            # 높이가 같거나 더 높은 곳이면 패스
            if graph[nx][ny] >= graph[x][y]:
                continue
            # 이전에 방문한 적이 없다면 큐에 삽입
            if not visited[nx][ny]:
                heapq.heappush(q, [-graph[nx][ny], nx, ny])
            visited[nx][ny] += visited[x][y]

m, n = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(n)] for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs()
print(visited[m-1][n-1])