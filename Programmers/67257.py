from collections import deque

def solution(expression):
    answer = 0
    opers = ['*', '+', '-']
    # 연산자 우선순위에 따른 3!개의 순열 생성
    priors = []
    for i in range(3):
        prior = [i]
        for j in range(3):
            if i != j:
                prior.append(j)
            if len(prior) == 3:
                priors.append(prior)
                break
        priors.append([i] + [prior[2]] + [prior[1]])

    # 숫자와 연산자를 구분하여 리스트로 재생성
    numbers = expression.replace('+', '-').replace('*', '-').split('-')
    data = []
    i = 0
    for num in numbers:
        i += len(num)
        data.append(int(num))
        if i < len(expression):
            data.append(expression[i])
            i += 1

    # 3! 경우의 수 반복문으로 모두 확인
    for prior in priors:
        left = [x for x in data]
        result = 0
        for i in prior:
            right = deque(left[1:])
            left = [left[0]]
            # 확인해야하는 연산자의 종류
            oper = opers[i]
            while left and right:
                if right[0] == oper:
                    right.popleft()
                    if oper == '*':
                        result = left.pop() * right.popleft()
                    if oper == '+':
                        result = left.pop() + right.popleft()
                    if oper == '-':
                        result = left.pop() - right.popleft()
                    left.append(result)
                else:
                    left.append(right.popleft())
                    if len(right) == 1:
                        left.append(right.popleft())

        answer = max(abs(result), answer)

    return answer
