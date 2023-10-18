import heapq
import sys
input = sys.stdin.readline

queue = []
n = int(input())
for i in range(1, n+1):
    num = int(input())
    heapq.heappush(queue, num)
    # 외친 수의 개수가 홀수개인 경우
    if i % 2 == 1:
        temp = []
        pop_num = i//2
        for _ in range(pop_num):
            temp.append(heapq.heappop(queue))
        print(queue[0])
        for data in temp:
            heapq.heappush(queue, data)
    if i % 2 == 0:
        temp = []
        pop_num = i//2 - 1
        for _ in range(pop_num):
            temp.append(heapq.heappop(queue))
        target = heapq.heappop(queue)
        if target<queue[0]:
            print(target)
        else:
            print(queue[0])
        heapq.heappush(queue, target)
        for data in temp:
            heapq.heappush(queue, data)
