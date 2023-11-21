'''선택된 번호를 기준으로 left, right 큐로 나눠서 풀이'''
# 효율성을 통과하기 위해 heapq 사용
from heapq import heappush, heappop

def solution(n, k, cmd):
    answer = ['O'] * n
    left = []
    right = []
    # 처음에 k행을 선택했으므로 k를 기준으로 left는 최대힙, right는 최소힙으로 관리하기
    for i in range(k+1):
        heappush(left, -i)
    for i in range(k+1, n):
        heappush(right, i)
    # 삭제된 행을 저장하는 리스트
    delete = []
    for req in cmd:
        req = req.split()
        oper = req[0]
        if oper == 'D':
            num = int(req[1])
            for _ in range(num):
                heappush(left, -heappop(right))
        elif oper == 'U':
            num = int(req[1])
            for _ in range(num):
                heappush(right, -heappop(left))
        elif oper == 'C':
            delete.append(-heappop(left))
            # 삭제된 행이 가장 마지막 행인 경우 고려
            if right:
                heappush(left, -heappop(right))
        elif oper == 'Z':
            num = delete.pop()
            if num > -left[0]:
                heappush(right, num)
            else:
                heappush(left, -num)

    for num in delete:
        answer[num] = 'X'
    answer = ''.join(answer)

    return answer
