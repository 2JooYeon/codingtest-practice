'''그리디를 이용한 풀이'''
def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = 0
    pickup = 0
    # 거리가 가장 먼 집부터 확인
    for i in range(n - 1, -1, -1):
        # 배달 및 수거할 물건 누적
        deliver += deliveries[i]
        pickup += pickups[i]

        # 남은 배달 및 수거할 물건이 없어질 때까지
        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            # 왕복 거리 계산
            answer += (i + 1) * 2

    return answer
