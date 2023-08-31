import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for _ in range(n):
    word = input().rstrip()
    stack = [word[0]]
    for i in range(1, len(word)):
        if len(stack) and stack[-1] == word[i]:
            stack.pop()
        else:
            stack.append(word[i])
    if len(stack) == 0:
        answer += 1
print(answer)
