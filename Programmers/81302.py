# BFS를 이용한 풀이
from collections import deque

def solution(places):
    answer = []
    # 상하좌우 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # x, y를 기준으로 거리두기를 잘 지켰는지 확인하는 함수
    def bfs(x, y):
        visited[x][y] = 1
        q = deque()
        q.append([x, y, 0])
        while q:
            x, y, cnt = q.popleft()
            if cnt == 2:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                    continue
                if not visited[nx][ny]:
                    if place[nx][ny] == 'P':
                        return False
                    if place[nx][ny] == 'O':
                        visited[nx][ny] = 1
                        q.append([nx, ny, cnt + 1])
        return True

    # 대기실에서 거리두기를 모두 잘 지켰는지 확인하는 함수
    def check():
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P' and bfs(i, j) == False:
                    return False
        return True

    for place in places:
        visited = [[0 for _ in range(5)] for _ in range(5)]
        # 잘 지켰으면 1
        if check():
            answer.append(1)
        # 한명이라도 안지켰으면 0
        else:
            answer.append(0)

    return answer
