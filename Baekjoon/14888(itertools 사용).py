from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
plus, sub, mul, div = map(int, input().split())

oper = ['+'] * plus + ['-'] * sub + ['*'] * mul + ['//'] * div
permu_oper = set(permutations(oper, len(oper)))
answer = []

for candi_oper in set(permu_oper):
    a = numbers[0]
    for i in range(len(candi_oper)):
        b = numbers[i+1]
        now_oper = candi_oper[i]
        if now_oper == '+':
            a += b
        if now_oper == '-':
            a -= b
        if now_oper == '*':
            a *= b
        if now_oper == '//':
            if a >= 0:
                a //= b
            else:
                a = -(abs(a)//b)
    answer.append(a)

print(max(answer))
print(min(answer))
