import heapq
import sys
input = sys.stdin.readline

max_heap, min_heap = [], []
n = int(input())
for _ in range(n):
    num = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    if len(max_heap) and len(min_heap) and -max_heap[0] > min_heap[0]:
        max_data = -heapq.heappop(max_heap)
        min_data = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -min_data)
        heapq.heappush(min_heap, max_data)
    print(-max_heap[0])