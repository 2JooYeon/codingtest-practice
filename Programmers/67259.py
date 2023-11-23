'''bfs를 이용해서 최소 비용 찾는 풀'''
from collections import deque

def solution(board):
    INF = int(1e9)
    answer = []
    # 상우하좌 (상하 방향은 인덱스가 짝수, 좌우 방향은 인덱스가 홀수)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # (x, y)까지 가는 비용 cost, d:0은 상하, d:1은 좌우
    def bfs(x,y,cost,d):
        q = deque()
        n = len(board)
        distance = [[INF]*n for _ in range(n)]
        distance[0][0] = 0
        q.append((x,y,cost,d))

        while q:
            x, y, cost, d = q.popleft()
            # 도착점에 도착한 경우 answer에 추가
            if x==n-1 and y==n-1:
                answer.append(cost)
                continue
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or nx>=n or ny<0 or ny>=n:
                    continue
                # 이동 후 방향 설정
                nd = 0
                if i % 2:
                    nd = 1
                # 이동 비용 설정
                ncost = cost+100
                if d!=nd:
                    ncost = cost+600

                if board[nx][ny] == 0:
                    # 기존보다 적은 비용으로 nx, ny에 갈 수 있는 경우만 큐에 추가
                    if ncost<distance[nx][ny]:
                        distance[nx][ny] = ncost
                        q.append((nx, ny, ncost, nd))
    bfs(0,0,0,0)
    bfs(0,0,0,1)

    return min(answer)
