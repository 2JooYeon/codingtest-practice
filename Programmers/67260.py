'''bfs를 이용한 풀이'''
from collections import deque
def solution(n, path, order):

    graph = [[] for _ in range(n)]
    # parent_child[i] = j -> i 노드에 도착해야 j 노드에 갈 수 있다.
    parent_child = {}
    # child_parent[j] = i -> j 노드에 도착하기 위해서는 i 노드에 가야 한다.
    child_parent = {}
    visited = [0] * n
    visited[0] = 1
    for a, b in path:
        # 양방향
        graph[a].append(b)
        graph[b].append(a)

    # a 노드에 방문한 후에 b 노드에 방문할 수 있다.
    for a, b in order:
        parent_child[a] = b
        child_parent[b] = a
        # 노드 0이 유일한 입구기 때문에, 노드 0의 선행 노드가 있는 경우 출입이 불가능 -> False
        if b == 0:
            return False
        if a == 0:
            parent_child[a] = 0

    q = deque([0])

    while q:
        now = q.popleft()
        # now로 가기 위한 선행 노드가 있고, 아직 선행 노드에 가지 않았을 때
        if now in child_parent and parent_child[child_parent[now]] != 0:
            visited[now] = 2
            continue
        for node in graph[now]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1
                # 현재 노드를 가고나서 갈 수 있는 노드들 탐색
                if node in parent_child:
                    target = parent_child[node]
                    parent_child[node] = 0
                    if visited[target] == 2:
                        q.append(target)
                        visited[target] = 1

    for i in visited:
        if i == 0:
            return False

    return True