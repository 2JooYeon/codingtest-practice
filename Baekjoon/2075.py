import heapq
n = int(input())
q = []
for _ in range(n):
    data = list(map(int, input().split()))
    for num in data:
        # 메모리 초과를 피하기 위해 큐의 크기를 n으로 제한
        if len(q) < n:
            heapq.heappush(q, num)
        else:
            if num > q[0]:
                heapq.heappop(q)
                heapq.heappush(q, num)
# 최소 힙이므로 0번째 원소 출력
print(q[0])