t = int(input())

def solution(d):
    for i in range(4, 11):
        d[i] += d[i-1]
        d[i] += d[i-2]
        d[i] += d[i-3]

data = []
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for _ in range(t):
    data.append(int(input()))

solution(d)

for n in data:
    print(d[n])

