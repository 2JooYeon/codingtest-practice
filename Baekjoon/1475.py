data = input()
num = [0 for _ in range(10)]

for n in data:
    num[int(n)] += 1

n = min(num[6], num[9])
s = (abs(num[6]-num[9])+1)//2

num[6] = n+s
num[9] = n+s
print(max(num))