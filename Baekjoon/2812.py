n, k = map(int, input().split())
nums = input()
stack = []
for num in nums:
    while k>0 and len(stack) and stack[-1] < num:
        stack.pop()
        k -= 1
    stack.append(num)

if k>0:
    stack = stack[:-k]
print(''.join(stack))
