import heapq

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

answer = 0
for _ in range(n-1):
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    answer += a+b
    heapq.heappush(card, a+b)

print(answer)