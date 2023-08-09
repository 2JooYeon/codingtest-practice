import heapq


def solution(food_times, k):
    answer = 0
    # 네트워크 장애 이전에 모든 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return -1

    # 이전 음식을 다 먹는데 걸리는 시간
    prev_time = 0
    q = []
    len_food = len(food_times)
    # 큐에 (시간, 음식 번호) 삽입
    for i in range(len_food):
        heapq.heappush(q, (food_times[i], i + 1))

    while k - ((q[0][0] - prev_time) * len_food) > 0:
        time = heapq.heappop(q)[0]
        k -= (time - prev_time) * len_food
        len_food -= 1
        prev_time = time

    # 음식 번호순으로 정렬
    sorted_num = sorted(q, key=lambda x: x[1])
    answer = sorted_num[k % len_food][1]

    return answer