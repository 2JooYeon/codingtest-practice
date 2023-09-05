import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    # 배열에 x를 추가하는 경우
    if x != 0:
        # 최대 힙이므로 음수 부호를 붙여서 추가
        heapq.heappush(q, -x)

    # 배열에서 가장 큰 값을 출력하고 값을 배열에서 제거하는 경우
    if x == 0:
        if len(q):
            data = heapq.heappop(q)
            print(-data)
        else:
            print(0)
