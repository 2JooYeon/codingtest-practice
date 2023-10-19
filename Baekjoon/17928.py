n = int(input())
data = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
    # 스택에 있는 수보다 더 큰 수를 만난 경우
    while stack and data[stack[-1]] < data[i]:
        # 오큰수로 저장
        answer[stack.pop()] = data[i]
    # 스택이 비어있거나, 자신보다 더 큰 수를 만나지 못한 경우
    stack.append(i)

print(' '.join(map(str, answer)))