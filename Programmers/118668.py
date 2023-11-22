'''현재 알고력과 코딩력에서 problems에서 가장 높은 알고력과 코딩력까지 도달하는 최단시간을 구하는 문제'''

# 풀이1: 다익스트라 알고리즘으로 풀이
import heapq
def solution(alp, cop, problems):
    answer = 0
    # 알고력과 코딩력을 1만큼 높이기 위해 1시간 공부를 하는 경우도 문제로 추가
    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]
    # 풀어야 하는 문제 중 가장 높은 코딩력 찾기
    problems.sort(key=lambda x: x[1])
    max_cop = problems[-1][1]
    # 풀어야 하는 문제 중 가장 높은 알고력 찾기
    problems.sort()
    max_alp = problems[-1][0]

    # distance[i][j] -> 알고력 i, 코딩력 j에 도달하기 위한 최단시간
    INF = int(1e9)
    distance = [[INF for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]

    # 초기 알고력과 코딩력이 목표 알고력과 코딩력보다 큰 경우 더 작은걸로 초기화
    alp, cop = min(alp, max_alp), min(cop, max_cop)
    distance[alp][cop] = 0
    queue = []
    # (시간, 알고력, 코딩력)
    heapq.heappush(queue, (0, alp, cop))

    while queue:
        # 현재의 소요시간, 알고력, 코딩력
        t, alp, cop = heapq.heappop(queue)
        if distance[alp][cop] < t:
            continue

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            # 알고력과 코딩력 두 값 모두 미달인 경우 이후 문제 볼 필요 없음
            if alp_req > alp and cop_req > cop:
                break
            # 알고력과 코딩력 둘 중 하나 미달인 경우, 현재 문제는 풀지 못하지만 이후 문제는 풀 수도 있으므로 continue
            elif alp_req > alp or cop_req > cop:
                continue

            # 문제를 풀고 늘어난 알고력과 코딩력
            new_alp = min(alp + alp_rwd, max_alp)
            new_cop = min(cop + cop_rwd, max_cop)

            if distance[alp][cop] + cost < distance[new_alp][new_cop]:
                distance[new_alp][new_cop] = distance[alp][cop] + cost
                heapq.heappush(queue, (distance[new_alp][new_cop], new_alp, new_cop))

    return distance[max_alp][max_cop]


# 풀이2: 다이나믹 프로그래밍으로 풀이
def solution(alp, cop, problems):
    # 풀어야 하는 문제 중 가장 높은 알고력과 코딩력 찾기
    problems.sort()
    max_alp = problems[-1][0]
    problems.sort(key=lambda x: x[1])
    max_cop = problems[-1][1]
    INF = int(1e9)
    # 2차원 DP 테이블 사용, dp[i][j] -> 알고력 i, 코딩력 j를 얻기 위해 필요한 최단 시간
    dp = [[INF for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 1의 시간을 들여서 알고리즘 공부나 코딩 공부를 하는 경우
            if i < max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            # 풀 수 있는 문제를 푸는 경우
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, max_alp)
                    new_cop = min(j + cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[max_alp][max_cop]
