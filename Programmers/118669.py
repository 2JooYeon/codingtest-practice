'''출입구에서 산봉우리까지의 최소 intensity 찾는 문제'''
# 다익스트라 알고리즘 이용
import heapq
def solution(n, paths, gates, summits):
    INF = int(1e9)
    intensity = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        # 양방향 그래프
        graph[i].append((j, w))
        graph[j].append((i, w))
    queue = []
    # 모든 출입구를 큐에 넣고 시작하기
    for gate in gates:
        intensity[gate] = 0
        # (intensity, 지점)
        heapq.heappush(queue, (0, gate))

    # 산봉우리에 도착했는지 빠르게 확인하기 위해 사전형 이용
    dict_summit = dict(zip(summits, [0] * len(summits)))

    while queue:
        dist, now = heapq.heappop(queue)
        # 산봉우리에 도착했거나, 이미 처리한 적이 있는 지점이면 continue
        if now in dict_summit or intensity[now] < dist:
            continue
        # 이동 가능한 지점중에 intensity 업데이트
        for node, weight in graph[now]:
            if intensity[node] > max(dist, weight):
                intensity[node] = max(dist, weight)
                heapq.heappush(queue, (intensity[node], node))

    # intensity가 최소가 되는 코스가 여러개라면, 산봉우리 번호가 작은 순서로 선택하기 위해 정렬
    summits.sort()
    min_intensity = INF
    for summit in summits:
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            min_summit = summit

    return [min_summit, min_intensity]
