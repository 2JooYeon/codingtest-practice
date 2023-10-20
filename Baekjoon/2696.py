import sys
input = sys.stdin.readline
import heapq

'''백준 1655번과 유사한 문제'''
t = int(input())
for _ in range(t):
    m = int(input())
    data = []
    div, mod = m//10, m%10
    for i in range(div):
        data += list(map(int, input().split()))
    if mod:
        data += list(map(int, input().split()))
    answer = []
    left_heap = []
    right_heap = []

    for i in range(1, m+1):
        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -data[i-1])
        else:
            heapq.heappush(right_heap, data[i-1])
        if right_heap and -left_heap[0] > right_heap[0]:
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
            heapq.heappush(left_heap, -heapq.heappop(right_heap))
        if i%2:
            answer.append(-left_heap[0])
    len_answer = len(answer)
    print(len_answer)
    for i in range(1, len(answer)+1):
        print(answer[i-1], end=' ')
        if i%10 == 0:
            print()