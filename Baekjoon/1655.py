# import heapq
# import sys
# input = sys.stdin.readline
#
# max_heap, min_heap = [], []
# n = int(input())
# for _ in range(n):
#     num = int(input())
#     if len(min_heap) == len(max_heap):
#         heapq.heappush(max_heap, -num)
#     else:
#         heapq.heappush(min_heap, num)
#     if len(max_heap) and len(min_heap) and -max_heap[0] > min_heap[0]:
#         max_data = -heapq.heappop(max_heap)
#         min_data = heapq.heappop(min_heap)
#         heapq.heappush(max_heap, -min_data)
#         heapq.heappush(min_heap, max_data)
#     print(-max_heap[0])

import sys
input = sys.stdin.readline
import heapq

# 왼쪽은 최대힙, 오른쪽은 최소힙 / left_heap의 0번째 값이 중간값이 되도록
left_heap = []
right_heap = []
n = int(input())
for _ in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    # 왼쪽힙의 0번 원소가 오른쪽힙의 0번원소보다 클 경우, 중간값 유지를 위해 swap
    if right_heap and -left_heap[0] > right_heap[0]:
        heapq.heappush(right_heap, -heapq.heappop(left_heap))
        heapq.heappush(left_heap, -heapq.heappop(right_heap))
    print(-left_heap[0])