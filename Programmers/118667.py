# 투포인터를 이용한 풀이
# queue1의 시작과 끝을 start, end로 놓고 구간합을 찾는 과정을 거친다.
def solution(queue1, queue2):
    answer = 0
    # queue1과 queue2를 합쳐서 하나의 큐로 만들기
    total_queue = queue1 + queue2
    # 총합이 홀수면 두 큐가 동일한 값을 가질 수 없음
    if sum(total_queue) % 2: return -1
    # 구간합 크기
    target = sum(total_queue) // 2
    n = len(total_queue)
    # queue1의 시작과 끝
    start, end = 0, n // 2
    # 현재 구간합
    interval_sum = sum(queue1)

    while start < n and end < n:
        if interval_sum < target:
            interval_sum += total_queue[end]
            end += 1
            answer += 1
        elif interval_sum > target:
            interval_sum -= total_queue[start]
            start += 1
            answer += 1
        else:
            return answer

    return -1


# 그리디를 활용한 풀이
# queue1의 합이 target보다 작으면 queue2의 원소를 추가하고, 합이 target보다 크면 queue1의 원소를 뺀다.
from collections import deque
def solution(queue1, queue2):
    answer = 0
    if (sum(queue1) + sum(queue2))%2: return -1
    target = (sum(queue1) + sum(queue2))//2
    total = sum(queue1)
    n = len(queue1)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    for _ in range(n*3):
        if total < target:
            data = queue2.popleft()
            queue1.append(data)
            total += data
            answer += 1
        elif total > target:
            data = queue1.popleft()
            queue2.append(data)
            total -= data
            answer += 1
        else:
            return answer
    return -1
