import heapq

def solution(food_times, k):
    # 네트워트 장애 발생 이전에 모든 음식을 섭취한 경우
    if sum(food_times) <= k:
        return -1

    total_time = 0
    prev_time = 0
    food_len = len(food_times)
    q = []

    for i in range(food_len):
        heapq.heappush(q, (food_times[i], i + 1))

    while total_time + ((q[0][0] - prev_time) * food_len) <= k:
        now_time = heapq.heappop(q)[0]
        total_time += (now_time - prev_time) * food_len
        prev_time = now_time
        food_len -= 1

    # 남은 음식 번호 기준으로 오름차순 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - total_time) % food_len][1]