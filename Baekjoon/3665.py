from collections import deque
t = int(input())


def topology_sort():
    result = []
    q = deque()
    # 위상 정렬의 결과가 하나인지 여부
    is_one = 1
    # 사이클이 발생하는지 여부
    is_cycle = 0

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어있으면 사이클 발생
        if len(q) == 0:
            is_cycle = 1
            break
        # 큐에 원소가 2개 이상 들어가면 정렬 결과가 여러개가 될 수 있음
        if len(q) >= 2:
            is_one = 0
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    return is_one, is_cycle, result



for _ in range(t):
    n = int(input())
    grade = list(map(int, input().split()))
    m = int(input())
    if m == 0:
        for x in grade:
            print(x, end=' ')
        print()
    else:
        graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
        indegree = [0] * (n+1)
        # 작년 순위 방향 그래프 초기화
        for i in range(n):
            for j in range(i+1, n):
                a = grade[i]
                b = grade[j]
                graph[a][b] = 1
                indegree[b] += 1
        # 올해 변경된 순위 정보
        for _ in range(m):
            a, b = map(int, input().split())
            # 간선 방향 반대로 뒤집기
            if graph[a][b]:
                graph[a][b] = 0
                graph[b][a] = 1
                indegree[a] += 1
                indegree[b] -= 1
            else:
                graph[a][b] = 1
                graph[b][a] = 0
                indegree[a] -= 1
                indegree[b] += 1

        is_one, is_cycle, result = topology_sort()
        if not is_one:
            print("?")
        elif is_cycle:
            print("IMPOSSIBLE")
        else:
            for x in result:
                print(x, end=' ')
            print()
