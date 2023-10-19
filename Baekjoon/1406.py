import sys
input = sys.stdin.readline
from collections import deque

# 커서를 기준으로 왼쪽, 오른쪽 스택을 둔다고 생각
left = deque(input().rstrip())
right = deque()
m = int(input())
for _ in range(m):
    query = input().split()
    c = query[0]
    if c == 'P':
        left.append(query[1])
    if c == 'L' and left:
        right.appendleft(left.pop())
    if c == 'D' and right:
        left.append(right.popleft())
    if c == 'B' and left:
        left.pop()

print(''.join(left) + ''.join(right))
