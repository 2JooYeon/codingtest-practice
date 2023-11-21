'''선택된 번호를 기준으로 left, right 큐로 나눠서 풀이'''
from collections import deque

def solution(n, k, cmd):
    answer = ['O'] * n
    data = list(range(0, n))
    # 처음에 k행을 선택했으므로 k를 기준으로 left, right 큐로 나누기
    left = deque(data[:k+1])
    right = deque(data[k+1:])
    # 삭제된 행을 저장하는 리스트
    delete = []
    for req in cmd:
        req = req.split()
        oper = req[0]
        if oper == 'D':
            num = int(req[1])
            for _ in range(num):
                left.append(right.popleft())
        elif oper == 'C':
            delete.append(left.pop())
            # 삭제된 행이 가장 마지막 행인 경우 고려
            if right:
                left.append(right.popleft())
        elif oper == 'U':
            num = int(req[1])
            for _ in range(num):
                right.appendleft(left.pop())
        elif oper == 'Z':
            num = delete.pop()
            if num > left[-1]:
                right.append(num)
                right = deque(sorted(right))
            else:
                left.append(num)
                left = deque(sorted(left))
    for num in delete:
        answer[num] = 'X'
    answer = ''.join(answer)

    return answer
