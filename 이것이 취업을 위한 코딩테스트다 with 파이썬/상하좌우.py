n = int(input())
plan = input().split()
x = 0
y = 0

for p in plan:
    if p == 'R' and y+1 < n:
        y += 1
    if p == 'L' and y-1 >= 0:
        y -= 1
    if p == 'U' and x-1 >= 0:
        x -= 1
    if p == 'D' and x+1 < n:
        x += 1

print(x+1, y+1)
