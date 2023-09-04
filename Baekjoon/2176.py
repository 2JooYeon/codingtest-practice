import heapq


def dijkstra(start):
    q = []
    # 시작 노드의 최단경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # start에서 현재까지 이동거리와 현재 노드
        dist, now = heapq.heappop(q)
        # 이전에 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 노드 확인
        for node, value in graph[now]:
            cost = dist + value
            # 현재 노드를 거쳐 다음 노드로 이동하는 거리 < start에서 다음 노드로 바로 이동하는 거리인 경우
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
            # 현재 노드에서 start 까지의 거리가 다음 노드에서 start까지의 거리보다 크다면, 합리적인 경로
            if dist > distance[node]:
                dp[now] += dp[node]

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 가능한 합리적인 경로의 개수
dp = [0 for _ in range(n+1)]
dp[2] = 1

# 역으로 2번 노드에서 출발
dijkstra(2)
print(dp[1])