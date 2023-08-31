import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque([home])
    while q:
        x, y = q.popleft()
        # 현재 위치에서 페스티벌까지 갈 수 있는 경우
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print("happy")
            return
        else:
            for i in range(n):
                if not visited[i]:
                    # 현재 위치에서 편의점까지 갈 수 있는 경우
                    if abs(x - store[i][0]) + abs(y - store[i][1]) <= 1000:
                        visited[i] = 1
                        q.append(store[i])
    print("sad")
    return


t = int(input())
for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(list(map(int, input().split())))
    festival = list(map(int, input().split()))
    visited = [0 for _ in range(n)]
    bfs()