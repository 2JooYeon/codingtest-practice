'''첫 번째 열(start_col), 마지막 열(end_col), 두 열을 제외한 행들(rows)
3개의 데이터를 각각 저장해서 deque 연산을 진행하는 풀이'''
from collections import deque

def solution(rc, operations):
    def shiftrow():
        start_col.appendleft(start_col.pop())
        end_col.appendleft(end_col.pop())
        rows.appendleft(rows.pop())

    def rotate():
        rows[0].appendleft(start_col.popleft())
        end_col.appendleft(rows[0].pop())
        rows[-1].append(end_col.pop())
        start_col.append(rows[-1].popleft())

    answer = []
    n = len(rc)
    start_col = deque()
    end_col = deque()
    rows = deque()
    for row in rc:
        start_col.append(row[0])
        rows.append(deque(row[1:-1]))
        end_col.append(row[-1])

    for oper in operations:
        if oper == 'Rotate':
            rotate()
        if oper == 'ShiftRow':
            shiftrow()

    for i in range(n):
        answer.append([start_col[i]] + list(rows[i]) + [end_col[i]])

    return answer
