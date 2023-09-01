t = int(input())

for _ in range(t):
    data = input()
    if data[0] == ')':
        print("NO")
        continue
    stack = [data[0]]
    flag = 0
    for i in range(1, len(data)):
        if len(stack) and stack[-1] != data[i]:
            stack.pop()
        elif len(stack) == 0 and data[i] == ')':
            print("NO")
            flag = 1
            break
        else:
            stack.append(data[i])
    if not flag:
        if len(stack):
            print('NO')
        else:
            print('YES')